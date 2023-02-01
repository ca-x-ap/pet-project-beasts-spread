const getParent = (beast, index) => beast[index] === null && beast[index] !== undefined
	? beast
	: getParent(beast[index], index);
const getNum = num => Math.round(Math.random(num));
const getRandNum = (max = 1, min = 0) => Math.round(Math.random() * (max - min) + min);

const makeStartBeasts = (array, count, time) => {
  for (var i = 0; i < count; i++) {
    var numberOfBeastList = getRandNum();
    array.live[numberOfBeastList].push({
      id: array.live[numberOfBeastList].length,
      // id0: null,
      // id1: null,
			0: null,
			1: null,
      time,
      gen: '000000'.replaceAll('0', () => getRandNum(9, 0)),
    });
  }

  // console.table(Object
  //     .keys(array.live[0][0])
  //     .map(keys => ({
  //       [keys]: array.live[0]
  //         .reduce((summ, el) =>
  //           ((summ < el[keys] && (summ += el[keys])), summ),
  //           ''
  //         )
  //     }))); // log start array

  return array;
};

const spread = (beasts, { maxLiveTime = 2, spreadCountTimes = 10, startCount = 20, maxChildrenCount = 2 }) => {
  var time = new Date().getFullYear();

  makeStartBeasts(beasts, startCount, time);

  for (var spreadCount = 0; spreadCount < spreadCountTimes; spreadCount++) {
    time++;

    if (beasts.live[0].length + beasts.live[1].length === 0) debugger;

    for (var i = 0; i < beasts.live[1].length; i++) {
      if (beasts.live[1][i] === undefined) continue;
      if ((beasts.live[1][i].time + getRandNum(maxLiveTime, 1)) < time ) {
        beasts.death[1].push(beasts.live[1][i]);
        beasts.live[1].splice(i, 1);
        i--;
      }
    }

    var beastsLive_1Copy = [...beasts.live[1]];

    for (var i = 0; i < beasts.live[0].length; i++) {
      if ((beasts.live[0][i].time + getRandNum(maxLiveTime, 1)) < time) {
        beasts.death[0].push(beasts.live[0][i]);
        beasts.live[0].splice(i, 1); // здесь я удаляю эллемент массива
				/**
				 * После удаления эллемента массива длина массива становиться length - 1
				 * Соответсвено нужно уменьшьать итератор, который подставляеться как идекс элемента массива
				 */
        i--;
        continue;
      }

      var parent = beasts.live[0][i];
      var partnerNum = getRandNum(beastsLive_1Copy.length - 1);
      var partnerBeast = beastsLive_1Copy[partnerNum];
      if (partnerBeast === undefined) continue;
      beastsLive_1Copy.splice(partnerNum, 1);

      // var countOfChildren = getNum(maxChildrenCount) + 1;

      for (var j = 0; j < maxChildrenCount; j++) {
        var numberOfBeastList = getRandNum();
        beasts.live[numberOfBeastList].push({
          id: beasts.live[numberOfBeastList].length,
          // id0: parent.id,
          // id1: partnerBeast.id,
					0: beasts.live[0][i],
          1: beastsLive_1Copy[partnerNum],
          time,
          gen: (numberOfBeastList === 0 ? parent : partnerBeast).gen.substring(0, 3) + (numberOfBeastList === 0 ? partnerBeast : parent).gen.substring(3, 6),
        });
      }
    }
  }

  return beasts;
}

const convertNumbers = num => new Intl.NumberFormat().format(num).replaceAll(',', '_');

const updateBeasts = (__, name, options = {}) => {
  const beasts = spread({ live: [[], []], death: [[], []] }, options = options || {});

  (() => {
		const liveStat = [...JSON.parse(localStorage.getItem('liveStat')) || [], convertNumbers(beasts.live[0].length + beasts.live[1].length)];
		localStorage.setItem('liveStat', JSON.stringify(liveStat));
		const deathStat = [...JSON.parse(localStorage.getItem('deathStat')) || [], convertNumbers(beasts.death[0].length + beasts.death[1].length)];
		localStorage.setItem('deathStat', JSON.stringify(deathStat));
		const l$dStat = [...JSON.parse(localStorage.getItem('l$dStat')) || [], convertNumbers(beasts.live[0].length - beasts.death[0].length + beasts.live[1].length - beasts.death[1].length)];
		localStorage.setItem('l$dStat', JSON.stringify(l$dStat));

    name = `${ name || 'Beasts' } <${ new Date().getMinutes() }:${ new Date().getSeconds() }> | <${ liveStat[liveStat.length - 1] }|${ deathStat[deathStat.length - 1] }|${ l$dStat[l$dStat.length - 1] }>`;
    console.group(name);
    console.table({ ...beasts /*, LiveStat: liveStat, DeathStat: deathStat, 'Live - Death stat': l$dStat */ });
    console.groupEnd(name);
  }) ();

  (() => {
    const divs = [document.createElement('div'), document.createElement('div')];
    // divs[0].style.backgroundColor = 'green';
    // divs[1].style.backgroundColor = 'red';
    divs[0].classList.add('container-a');
    divs[1].classList.add('container-a');

    const addOnPage = (arr, index) => arr.forEach(beast => {
      const div = document.createElement('div');
      div.style.backgroundColor = '#' + beast.gen;
      div.classList.add('beast');
      divs[index].append(div);
    });

    addOnPage(beasts.live[0].splice(0, beasts.live[0].length), 0);
    addOnPage(beasts.live[1].splice(0, beasts.live[1].length), 1);

    animals.innerHTML = '';
    animals.append(...divs);
  }) () // run ()

	return beasts;
};

const beasts = updateBeasts();
update_info.addEventListener('click', () => {
	animals.innerHTML = ''
	progress.style.display = '';
	setTimeout(() => updateBeasts('', '', { spreadCountTimes: spreadCountTimes.value }), 2000)
	// .then(() => progress.style.display = 'none');
	setTimeout(() => progress.style.display = 'none', 2000)

}, false);

// setInterval(() => updateBeasts(), 1000);

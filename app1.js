var getNum = num => Math.round(Math.random(num));
var makeStartBeasts = (array, count, time) => {
  for (var i = 0; i < count; i++) {
    var numberOfBeastList = getNum(1);
    array.live[numberOfBeastList].push({
      id: array.live[numberOfBeastList].length,
      id0: null,
      id1: null,
      time,
      gen: [getNum(9), getNum(9), getNum(9), getNum(9), getNum(9), getNum(9)].join(''),
    });
  }

  console.table(Object
      .keys(array.live[0][0])
      .map(keys => ({
        [keys]: array.live[0]
          .reduce((summ, el) =>
            ((summ < el[keys] && (summ += el[keys])), summ),
            ''
          )
      }))); // log start array

  return array;
};

const spread = (beasts, { maxLiveTime = 2, spreadCountTimes = 22, startCount = 20, maxChildrenCount = 2 }) => {
  var time = 0;

  makeStartBeasts(beasts, startCount, time);

  for (var spreadCount = 0; spreadCount < spreadCountTimes; spreadCount++) {
    time++;

    if (beasts.live[0].length + beasts.live[1].length === 0) debugger;

    for (var i = 0; i < beasts.live[1].length; i++) {
      if (beasts.live[1][i] === undefined) continue;
      if ((beasts.live[1][i].time + getNum(maxLiveTime) + 1) < time ) {
        beasts.death[1].push(beasts.live[1][i]);
        beasts.live[1].splice(i, 1);
        i--;
      }
    }

    var beastsLive_1Copy = [...beasts.live[1]];

    for (var i = 0; i < beasts.live[0].length; i++) {
      if ((beasts.live[0][i].time + getNum(maxLiveTime) + 1) < time) {
        beasts.death[0].push(beasts.live[0][i]);
        beasts.live[0].splice(i, 1);
        i--;
        continue;
      }

      var parent = beasts.live[0][i];
      var partnerNum = getNum(beastsLive_1Copy.length - 1);
      var partnerBeast = beastsLive_1Copy[partnerNum];
      if (partnerBeast === undefined) continue;
      beastsLive_1Copy.splice(partnerNum, 1);

      // var countOfChildren = getNum(maxChildrenCount) + 1;

      for (var j = 0; j < maxChildrenCount; j++) {
        var numberOfBeastList = getNum(1);
        beasts.live[numberOfBeastList].push({
          id: beasts.live[numberOfBeastList].length,
          id0: parent.id,
          id1: partnerBeast.id,
          time,
          gen: (numberOfBeastList === 0 ? parent : partnerBeast).gen.substring(0, 3) + (numberOfBeastList === 0 ? partnerBeast : parent).gen.substring(3, 6),
        });
      }
    }
  }

  return beasts;
}

const convertNumbers = num => (num + '')
  .split('')
  .reverse()
  .reduce((accumulator, currentValue, currentIndex) => 
    (accumulator.push(currentValue), (currentIndex + 1 % 3 === 0) && accumulator.push('_'), accumulator), [])
  .reverse()
  .join('');

const updateBeasts = name => {
  const beasts = spread({ live: [[], []], death: [[], []] }, {});

  (() => {
    name = `${ name || 'Beasts' } <${ new Date().getMinutes() }:${ new Date().getSeconds() }>`
    console.group(name);
    console.table({ 
      'Live': convertNumbers(beasts.live[0].length + beasts.live[1].length), 
      'Death': convertNumbers(beasts.death[0].length + beasts.death[1].length)
    });
    console.table(beasts);
    console.groupEnd(name);
  }) ();

  (() => {
    const divs = [document.createElement('div'), document.createElement('div')];
    divs[0].style.backgroundColor = 'green';
    divs[1].style.backgroundColor = 'red';
    divs[0].classList.add('container');
    divs[1].classList.add('container');
  
    const addOnPage = (arr, index) => arr.forEach(beast => {
      const div = document.createElement('div');
      div.style.backgroundColor = '#' + beast.gen;
      div.classList.add('beast');
      divs[index].append(div);
    });
  
    addOnPage(beasts.live[0].splice(0, beasts.live[0].length), 0);
    addOnPage(beasts.live[1].splice(0, beasts.live[1].length), 1);
  
    document.body.innerHTML = '';
    document.body.append(...divs);
  }) // run ()
};

updateBeasts();

// setInterval(() => updateBeasts(), 1000);

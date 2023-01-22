const spread = ({ maxLiveTime, spreadCountTimes }) => {
  var beasts = { live: [[], []], death: [[], []] };
  var getNum = num => Math.round(Math.random(num));
  var unixTime = 0;

  for (let i = 0; i < 100; i++) {
    var numberOfBeastList = getNum(1);
    beasts.live[numberOfBeastList].push({
      id: beasts.live[numberOfBeastList].length,
      id0: null,
      id1: null,
      unixTime: unixTime + getNum(maxLiveTime),
    });
  }

  for (let spreadCount = 0; spreadCount < spreadCountTimes /*|| beasts.live[0].length === 0 || beasts.live[1].length === 0 */; spreadCount++) {
    unixTime++;

    for (var i = 0; i < beasts.live[1].length; i++) {
      if (beasts.live[1][i] === undefined) continue;
      if (beasts.live[1][i].unixTime < unixTime) {
        beasts.death[1].push(beasts.live[1][i]);
        beasts.live[1].splice(i, 1);
        i--;
      }
    }

    var beastsLive_1Copy = JSON.parse(JSON.stringify(beasts.live[1]));

    for (var i = 0; i < beasts.live[0].length; i++) {
      if (beasts.live[0][i].unixTime < unixTime) {
        beasts.death[0].push(beasts.live[0][i]);
        beasts.live[0].splice(i, 1);
        i--;
        continue;
      }

      var partnerNum = getNum(beastsLive_1Copy.length - 1);
      var partnerBeast = beastsLive_1Copy[partnerNum];
      if (partnerBeast === undefined) continue;
      beastsLive_1Copy.splice(partnerNum, 1);

      var countOfChildren = getNum(3) + 1;

      for (let j = 0; j < countOfChildren; j++) {
        var numberOfBeastList = getNum(2);
        beasts.live[numberOfBeastList].push({
          id: beasts.live[numberOfBeastList].length,
          id0: beasts.live[0][index].id,
          id1: partnerBeast.id,
          unixTime: unixTime + getNum(maxLiveTime) + 1,
        });
      }
    }
  }

  return beasts;
}

const beasts = spread({ maxLiveTime: 5, spreadCountTimes: 10 });
console.group('Beasts');
console.table(beasts);
console.groupEnd('Beasts');
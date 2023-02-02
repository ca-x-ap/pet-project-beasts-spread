// d3.select("#d3_animals").append("p").text("Hello World!");


  //   d3.select("#d3_animals")
  //   // d3.select("body")
  // .selectAll("p")
  // .data([4, 8, 15, 16, 23, 42])
  // .enter().append("p")
  //   .text(function(d) { return "I’m number " + d + "!"; });


  // var p = d3.select("#d3_animals")
    //   .selectAll("p")
    //   .data([4, 8, 15, 16, 23, 42])
    //     .text(function(d) { return d; });

    // // Enter…
    // p.enter().append("p")
    //     .text(function(d) { return d; });

    // // Exit…
    // p.exit().remove();


    // d3.select("#d3_animals").selectAll("circle").transition()
    //   .duration(750)
    //   .delay(function(d, i) { return i * 10; })
    //   .attr("r", function(d) { return Math.sqrt(d * scale); });

    // flare = FileAttachment("flare.json").json();

    // Tree = ƒ(sdds)

    // import { Tree } from "@d3/tree"

    var flare = {
      name: 'flare',
      children: [
        { name: 'analitycs', children: [{ name: 'analitycs', children: [{ name: 'analitycs', children: [] }] }, { name: 'analitycs', children: [] }] },
        { name: 'analitycs', children: [{ name: 'analitycs', children: [] }] },
        { name: 'analitycs', children: [] },
        { name: 'analitycs', children: [{ name: 'analitycs', children: [] },{ name: 'analitycs', children: [] },{ name: 'analitycs', children: [{ name: 'analitycs', children: [] },{ name: 'analitycs', children: [] },{ name: 'analitycs', children: [{ name: 'analitycs', children: [] }] }] }] },
      ]
    };

    chart = Tree(flare, {
      label: d => d.name,
      title: (d, n) => `${n.ancestors().reverse().map(d => d.data.name).join(".")}`, // hover text
      link: (d, n) => `https://github.com/prefuse/Flare/${n.children ? "tree" : "blob"}/master/flare/src/${n.ancestors().reverse().map(d => d.data.name).join("/")}${n.children ? "" : ".as"}`,
      width: 1152
    });

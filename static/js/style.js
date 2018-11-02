$("#ModalPredictionInput").on('show.bs.modal', function(){
    alert("Hello World!");
  });


  // to display the graphic pictures
  var svgWidth=600,svgHeight =300, radius =  Math.min(svgWidth, svgHeight) / 2;
  var margin = {top: 40, right: 20, bottom: 30, left: 40},
      width = svgWidth- margin.left - margin.right,
      height = svgHeight - margin.top - margin.bottom;

  var svgChart=d3.select('svg')
              .attr('width',svgWidth)
              .attr('height',svgHeight)
              .attr("transform", `translate(${margin.left}, ${margin.top})`);

  var xScale=d3.scaleOrdinal()
              .range([0,width],.5)

  var yScale=d3.scaleLinear()
              .range([height,0])

  var x_axis=d3.axisBottom(xScale)
  var y_axis=d3.axisLeft(yScale)
  var color = d3.scaleOrdinal(d3.schemeCategory10);
  console.log('it works')
  //plot the data
  d3.json('api/gender').then(function(genderCountsData){
    console.log(`the gender data is ${genderCountsData} `)
    console.log('it works')
    //apendx axes to the chart
    // svgChart.append('g')
    //         .call(x_axis)

    // svgChart.append('g')
    //         .call(y_axis)

    var path=d3.arc()
      .outRadius(radius)
      .innerRadius(0)
    
    var pieValue =d3.pie().value(d=>d.Counts)
    var pieChart=svgChart.select('arc')
                 .data(pie(genderCountsData))
                 .enter()
                 .append('g')
    var label = d3.arc()
                 .outerRadius(radius)
                 .innerRadius(0);
    pieChart.append('path')
            .attr('d', path)
            .attr('fill',d=>color(genderCountsData.gender))
    
    pie.append("text")
        .attr("transform", function(d) { 
                return "translate(" + label.centroid(d) + ")"; 
            })
            .attr("text-anchor", "middle")
            .text(function(d){ return genderCountsData.gener+":"+genderCountsData.Counts; });        
  })

console.log("Welcome to our Dashboard, We are getting data from MYSQL  database and generating Javascript Plotly!!");

let plot1_url = `/default/bygender`;
let plot2_url = `/default/sept_delays`;
let plot_age = `/api/age_bal`;
let plot_pop = `/population/summary`;

function byGender(){
  d3.json(plot1_url).then((data) => {
    console.log(data);
    // create a gender array

    const gender = [];

    gender.push('female')
    gender.push('male')

    const total_cc_default = [];
    total_cc_default.push(data[0]['total_num_CC_default'])
    total_cc_default.push(data[1]['total_num_CC_default'])

    console.log(total_cc_default);
    // console.log(data);
  var pieData = [
    {
      values: total_cc_default, // should look like => [14349, 9015]
      labels: gender,
      hovertext: gender,
      hoverinfo: "hovertext",
      type: "pie"
    }
  ];

  var pieLayout = {
    margin: { t: 0, l: 0 }
  };

  Plotly.plot("pie", pieData, pieLayout);
  console.log("*******");
});
}

function sept_delayedPayments(){
  d3.json(plot2_url).then((data) => {
    console.log(data);
    const num_acc=[];
    const months =[];
    for(var i=0; i<data.length;i++){
      num_acc.push(data[i]['number_of_accounts'])
      months.push(data[i]['months_delayed_since_Sept'])
    }
    console.log('this is num_acc', num_acc);

    var layout = {
      margin:{t:0},
      hovermode:"closest",
      xaxis:{title:"Number of Months delayed"}, 
      yaxis:{title:"Number of Accounts"}
    };
    
    var data = [{
      x: months,
      y: num_acc, 
      type: 'bar',
      mode: "markers",
      marker: {
        colorscale: "Portland"
      }
    }];
    Plotly.newPlot("bar", data, layout)      
});     
}

function plotAge(){
  d3.json(plot_age).then((data)=>{
  console.log(data)

  const age_grp = [];
  const avg_credit = [];

  for(var i=0; i<data.length; i++)
  {
    age_grp.push(data[i]['age'])
    avg_credit.push(data[i]['avg_credit_granted'])
  }

  var layout = {
    margin:{t:0},
    hovermode:"closest",
    xaxis:{title:"Age Group"}, 
    yaxis:{title:"Average Credit Granted"}
  };
  var data = [{
    x: age_grp,
    y: avg_credit, 
    type: 'line',
    // text: x,
    //mode: 'lines'
  }];
  Plotly.newPlot("line", data, layout); 
  });
  
}


function pop_sum(){
  d3.json(plot_pop).then((data)=>{
  console.log(data)

  const age = [];
  const num_recs = [];

  for(var i=0;i<data.length;i++)
  {
    age.push(data[i]['age'])
    num_recs.push(data[i]['number_of_records'])
  }

  var layout = {
    margin:{t:0},
    hovermode:"closest",
    xaxis:{title:"Age Group"}, 
    yaxis:{title:"Number of Records"}
  };
  var trace1 = {
    x: age,
    y: num_recs, 
    mode: 'markers',
    type: 'scatter'
  };
  var data = [trace1];

  Plotly.newPlot("bubbles", data, layout);
  });
}



 function init() {
   byGender();
   sept_delayedPayments();
   plotAge();
   pop_sum();
 }

 init();






//   var pielayout = {
//     margin:{t:0, l:0}
//    }
 
//    var data = [{
//     values: male.slice(0,len(num_recs)),
//     labels: num_recs.slice(0,len(num_recs)), 
//     hovertext: num_recs.slice(0,len(num_recs)),
//     hover_info: "hovertext",
//     type:'pie'
//    }];
//    Plotly.newPlot("pie", data,pielayout);
//  });
//  }



//  function init() {

//       byGender();
//  }
//  init();
console.log("Welcome to our Dashboard, We are getting data from MYSQL  database and generating Javascript Plotly!!");

let plot1_url = `/default/bygender`;
let plot2_url = `/default/sept_delays`;

function byGender(){
  d3.json(plot1_url).then((data) => {
    console.log(data);
    // create a gender array

    const gender = [];
    // gender.push(data[0]['male'])
    // gender.push(data[1]['male'])

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
  })
};
//     const i = 0; 
//     const num_mos = [];
//     const num_acc = [];

//     data.forEach(element => {
      
//     });
//     //   num_mos.push(data[i]['months_delayed_since_September'])
//     //   num_acc.push(data[i]['number_of_accounts'])
//     // }
//     var layout = {
//       margin:{t:0},
//       hovermode:"closest",
//       xaxis:{title:"Number of Months Dealayed"}, 
//       yaxis:{title:"Number of Credit Card Accounts"}
//     };

//     var trace1 = {
//       x: area_names,
//       y: num_acc,
//       mode: 'markers',
//       marker: {
//         // size: [40, 60, 80, 100]
//       }
//     };
    
//     var data = [trace1];
//     Plotly.newPlot("bubbles", data, layout);
//   })
// }


 function init() {
   //console.log('byGender:', byGender)
   byGender();
   sept_delayedPayments();
   //
   //
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
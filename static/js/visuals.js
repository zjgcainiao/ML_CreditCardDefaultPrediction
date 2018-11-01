console.log("Welcome to our Dashboard, We are getting data from MYSQL  database and generating Javascript Plotly!!");

function byGender(){
 d3.json("/default/bygender").then((data) => {
  const male = data.male;
  const num_recs = data.total_num_CC_default;
  const col_id = [120,125,130,135,140,145,150,155]
  console.log(male)


  var pielayout = {
    margin:{t:0, l:0}
   }
 
   var data = [{
    values: male.slice(0,len(num_recs)),
    labels: num_recs.slice(0,len(num_recs)), 
    hovertext: num_recs.slice(0,len(num_recs)),
    hover_info: "hovertext",
    type:'pie'
   }];
   Plotly.newPlot("pie", data,pielayout);
 });
 }



 function init() {

      byGender();
 }
 init();
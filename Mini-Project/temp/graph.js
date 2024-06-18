google.charts.load('current', {'packages':['corechart']});

// Draw the pie chart and bar chart when Charts is loaded.
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Work', 3],
    ['eat', 1],
    ['movie', 1],
    ['class', 1],
    ['workout', 2]
  ]);

  //piechart
  var piechart_options = {title:'Data',
                 width:400,
                 height:300};
  var piechart = new google.visualization.PieChart(document.getElementById('piechart_div'));
  piechart.draw(data, piechart_options);
//piechart end

//barchart
  var barchart_options = {title:'Data',
                 width:400,
                 height:300,
                 legend: 'none'};
  var barchart = new google.visualization.BarChart(document.getElementById('barchart_div'));
  barchart.draw(data, barchart_options);
//barchart end
}
line_chart_data = [];

function receiveLineChartData() {
    $.ajax({
        url: "/chart_data/LINE",
        type: "GET",
        crossDomain: true,
        async: false,
        contentType: "application/json;charset=utf-8",
        accept: "application/json;charset=utf-8",
        dataType: "json",
        success: function (l_d) {

            var line_chart_headers = [];
            
            for (l_i in l_d.headers) {
                line_chart_headers.push(l_d.headers[l_i]);
            }
            line_chart_data[0] = line_chart_headers;

            var l_index = 1;
            for (l_i in l_d.data) {
                l_temp_data = [];

                l_idx = 0;
                for (l_j in l_d.data[l_i]) {
                    if (l_idx == 0)
                        l_temp_data[l_idx] = parseInt(l_d.data[l_i][l_j]);
                    else
                        l_temp_data[l_idx] = parseInt(l_d.data[l_i][l_j]);

                    l_idx += 1;
                }

                line_chart_data[l_index] = l_temp_data;
                l_index += 1;
            }
        },

        error: function (d) {
            alert("Error" + d);
        },

        complete: function (d) {
        },

        beforeSend: function (xhr) {
            xhr.setRequestHeader(
                "Access-Control-Allow-Origin",
                "localhost:8000"
            );
        },
    });
}

function drawLineChart() {
    receiveLineChartData();
    
    var l_data = new google.visualization.DataTable();
    l_data.addColumn("number", line_chart_data[0][0]);
    l_data.addColumn("number", line_chart_data[0][1]);

    for (let l_i = 1; l_i < line_chart_data.length; l_i++) {
        l_data.addRow([
            line_chart_data[l_i][0],
            line_chart_data[l_i][1]
        ]);
    }

    var l_options = {
        title: "Release Year Counts"
    };

    var lineChart = new google.visualization.LineChart(
        document.getElementById("line_chart_dimensions")
    );

    lineChart.draw(l_data, l_options);
}

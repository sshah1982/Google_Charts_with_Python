area_chart_data = [];

function receiveAreaChartData() {
    $.ajax({
        url: "/chart_data/AREA",
        type: "GET",
        crossDomain: true,
        async: false,
        contentType: "application/json;charset=utf-8",
        accept: "application/json;charset=utf-8",
        dataType: "json",
        success: function (a_d) {
            a_chart_headers = [];

            for (a_i in a_d.headers) {
                a_chart_headers.push(a_d.headers[a_i]);
            }
            area_chart_data[0] = a_chart_headers;

            a_index = 1;
            for (a_i in a_d.data) {
                a_temp_data = [];

                a_idx = 0;
                for (a_j in a_d.data[a_i]) {
                    if (a_idx == 0)
                        a_temp_data[a_idx] = a_d.data[a_i][a_j];
                    else
                        a_temp_data[a_idx] = parseInt(a_d.data[a_i][a_j]);

                    a_idx += 1;
                }

                area_chart_data[a_index] = a_temp_data;
                a_index += 1;
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

function drawAreaChart() {
    receiveAreaChartData();

    var a_data = new google.visualization.DataTable();
    a_data.addColumn("string", area_chart_data[0][0]);
    a_data.addColumn("number", area_chart_data[0][1]);

    for (let a_i = 1; a_i < area_chart_data.length; a_i++) {
        a_data.addRow([
            area_chart_data[a_i][0],
            area_chart_data[a_i][1]
        ]);
    }

    var a_options = {
        title: "IMDB Movies Ratings Counts"
    };

    var areaChart = new google.visualization.AreaChart(
        document.getElementById("area_chart_dimensions")
    );

    areaChart.draw(a_data, a_options);

    drawPieChart();
}

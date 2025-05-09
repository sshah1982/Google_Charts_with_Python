pie_chart_data = [];

function receivePieChartData() {
    $.ajax({
        url: "/chart_data/PIE",
        type: "GET",
        crossDomain: true,
        async: false,
        contentType: "application/json;charset=utf-8",
        accept: "application/json;charset=utf-8",
        dataType: "json",
        success: function (p_d) {
            p_chart_headers = [];
            
            for (p_i in p_d.headers) {
                p_chart_headers.push(p_d.headers[p_i]);
            }
            pie_chart_data[0] = p_chart_headers;

            p_index = 1;
            for (p_i in p_d.data) {
                p_temp_data = [];

                p_idx = 0;
                for (p_j in p_d.data[p_i]) {
                    if (p_idx == 0)
                        p_temp_data[p_idx] = p_d.data[p_i][p_j];
                    else
                        p_temp_data[p_idx] = parseInt(p_d.data[p_i][p_j]);

                    p_idx += 1;
                }

                pie_chart_data[p_index] = p_temp_data;
                p_index += 1;
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

function drawPieChart() {
    receivePieChartData();

    var p_data = new google.visualization.DataTable();
    p_data.addColumn("string", pie_chart_data[0][0]);
    p_data.addColumn("number", pie_chart_data[0][1]);

    for (let p_i = 1; p_i < pie_chart_data.length; p_i++) {
        p_data.addRow([
            pie_chart_data[p_i][0],
            pie_chart_data[p_i][1]
        ]);
    }

    var p_options = {
        title: "IMDB Movies Ratings Counts"
    };

    var pieChart = new google.visualization.PieChart(
        document.getElementById("pie_chart_dimensions")
    );

    pieChart.draw(p_data, p_options);

    drawLineChart();
}

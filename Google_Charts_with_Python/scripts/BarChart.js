bar_chart_data = [];

function receiveBarChartData() {
    $.ajax({
        url: "/chart_data/BAR",
        type: "GET",
        crossDomain: true,
        async: false,
        contentType: "application/json;charset=utf-8",
        accept: "application/json;charset=utf-8",
        dataType: "json",
        success: function (b_d) {
            b_chart_headers = [];

            for (b_i in b_d.headers) {
                b_chart_headers.push(b_d.headers[b_i]);
            }
            bar_chart_data[0] = b_chart_headers;

            b_index = 1;
            for (b_i in b_d.data) {
                b_temp_data = [];

                b_idx = 0;
                for (b_j in b_d.data[b_i]) {
                    if (b_idx == 0)
                        b_temp_data[b_idx] = b_d.data[b_i][b_j];
                    else
                        b_temp_data[b_idx] = parseFloat(b_d.data[b_i][b_j]);

                    b_idx += 1;
                }

                bar_chart_data[b_index] = b_temp_data;
                b_index += 1;
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

function drawBarChart() {
    receiveBarChartData();

    var b_formatter = new google.visualization.NumberFormat({
        fractionDigits: 2
    });

    var b_data = new google.visualization.DataTable();
    b_data.addColumn("string", bar_chart_data[0][0]);
    b_data.addColumn("number", bar_chart_data[0][1]);

    for (let b_i = 1; b_i < bar_chart_data.length; b_i++) {
        b_data.addRow([
            bar_chart_data[b_i][0],
            bar_chart_data[b_i][1]
        ]);
    }

    b_formatter.format(b_data, 1);

    var b_options = {
        title: "Average Income by Country",
        width: 600,
        height: 400,
        bar: { groupWidth: "95%" },
        legend: { position: "none" },
        hAxis: { minValue: 0 }
    };

    var barChart = new google.visualization.BarChart(
        document.getElementById("bar_chart_dimensions")
    );

    barChart.draw(b_data, b_options);

    drawAreaChart();
}

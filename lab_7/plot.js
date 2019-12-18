$(document).ready(function () {
    $("button").click(function () {
        const from = $("#from");
        const to = $("#to");
        const func = $("#function");

        let points = [];

        for (let x = parseInt(from.val()); x <= parseInt(to.val()); x++) {
            points.push([x, eval(func.val())]);
        }

        let options = {
            legend: {
                show: true,
                position: "ne"
            }
         };

        let data = [
            {
                data: points,
                label: func.val().toString(),
                color: "lightgreen"
            }
        ]

        $.plot($("#plot"), data, options);
    });
});
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var $canvas = $("#canvas");
//alert($canvas);
var canvasOffset = $canvas.offset();
var offsetX = canvasOffset.left;
var offsetY = canvasOffset.top;
//alert("2");

var $0 = $("#0");
var $1 = $("#1");
var $2 = $("#2");
var $3 = $("#3");
var $4 = $("#4");
var $0r = $("#0r");
var $1r = $("#1r");
var $2r = $("#2r");
var $3r = $("#3r");
var $4r = $("#4r");
//alert("3");
var u1=[0.01726756775633201, 0.0006844757310517818, 0.002087307843321056, 0.001143460677398612, 0.0009413027407231592];
var u2=[0.0003499378618853585, 0.010117748659590399, 0.002379946026669582, 0.002043678350750612, 0.002216254465855732];
var u3=[0.006302527622991312, 0.002551390085739209, 0.0070097832091255965, 0.004064129266236546, 0.001582366529477463];
var u4=[0.0012146704477122392, 0.001449813879385265, 0.0016941689202413272, 0.013901345728444446, 0.0015908644629112612];
var u5=[0.0036723231926685763, 0.0015464721802407936, 0.00151282865197683, 0.0015995518503334237, 0.009120189500378387];

var connectors0 = [];
connectors0.push({
    from: $0,
    to: $0r
});
connectors0.push({
    from: $0,
    to: $1r
});
connectors0.push({
    from: $0,
    to: $2r
});
connectors0.push({
    from: $0,
    to: $3r
});
connectors0.push({
    from: $0,
    to: $4r
});
var connectors1 = [];
connectors1.push({
    from: $1,
    to: $0r
});
connectors1.push({
    from: $1,
    to: $1r
});
connectors1.push({
    from: $1,
    to: $2r
});
connectors1.push({
    from: $1,
    to: $3r
});
connectors1.push({
    from: $1,
    to: $4r
});

var connectors2 = [];
connectors2.push({
    from: $2,
    to: $0r
});
connectors2.push({
    from: $2,
    to: $1r
});
connectors2.push({
    from: $2,
    to: $2r
});
connectors2.push({
    from: $2,
    to: $3r
});
connectors2.push({
    from: $2,
    to: $4r
});
var connectors3 = [];
connectors3.push({
    from: $3,
    to: $0r
});
connectors3.push({
    from: $3,
    to: $1r
});
connectors3.push({
    from: $3,
    to: $2r
});
connectors3.push({
    from: $3,
    to: $3r
});
connectors3.push({
    from: $3,
    to: $4r
});
var connectors4 = [];
connectors4.push({
    from: $4,
    to: $0r
});
connectors4.push({
    from: $4,
    to: $1r
});
connectors4.push({
    from: $4,
    to: $2r
});
connectors4.push({
    from: $4,
    to: $3r
});
connectors4.push({
    from: $4,
    to: $4r
});

connect();

$(".draggable").draggable({
    // event handlers
    start: noop,
    drag: connect,
    stop: noop
});

function noop() {}

function connect() {
    //alert("connect");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (var i = 0; i < connectors0.length; i++) {
        var c = connectors0[i];
        var eFrom = c.from;
        var eTo = c.to;
        var pos1 = eFrom.offset();
        var pos2 = eTo.offset();
        var size1 = eFrom.size();
        var size2 = eTo.size();
        ctx.lineWidth = 0.5+u1[i]*500;
        ctx.beginPath();
        ctx.moveTo(pos1.left + eFrom.width() + 3, pos1.top + eFrom.height() / 2);
        ctx.lineTo(pos2.left + 5, pos2.top + eTo.height() / 2);
        ctx.stroke();

    }
    for (var i = 0; i < connectors1.length; i++) {
        var c = connectors1[i];
        var eFrom = c.from;
        var eTo = c.to;
        var pos1 = eFrom.offset();
        var pos2 = eTo.offset();
        var size1 = eFrom.size();
        var size2 = eTo.size();
        ctx.lineWidth = 0.5+u2[i]*500;
        ctx.beginPath();
        ctx.moveTo(pos1.left + eFrom.width() + 3, pos1.top + eFrom.height() / 2);
        ctx.lineTo(pos2.left + 5, pos2.top + eTo.height() / 2);
        ctx.stroke();

    }
    for (var i = 0; i < connectors2.length; i++) {
        var c = connectors2[i];
        var eFrom = c.from;
        var eTo = c.to;
        var pos1 = eFrom.offset();
        var pos2 = eTo.offset();
        var size1 = eFrom.size();
        var size2 = eTo.size();
        ctx.lineWidth = 0.5+u3[i]*500;
        ctx.beginPath();
        ctx.moveTo(pos1.left + eFrom.width() + 3, pos1.top + eFrom.height() / 2);
        ctx.lineTo(pos2.left + 5, pos2.top + eTo.height() / 2);
        ctx.stroke();

    }
     for (var i = 0; i < connectors3.length; i++) {
        var c = connectors3[i];
        var eFrom = c.from;
        var eTo = c.to;
        var pos1 = eFrom.offset();
        var pos2 = eTo.offset();
        var size1 = eFrom.size();
        var size2 = eTo.size();
        ctx.lineWidth = 0.5+u4[i]*500;
        ctx.beginPath();
        ctx.moveTo(pos1.left + eFrom.width() + 3, pos1.top + eFrom.height() / 2);
        ctx.lineTo(pos2.left + 5, pos2.top + eTo.height() / 2);
        ctx.stroke();

    }
     for (var i = 0; i < connectors4.length; i++) {
        var c = connectors4[i];
        var eFrom = c.from;
        var eTo = c.to;
        var pos1 = eFrom.offset();
        var pos2 = eTo.offset();
        var size1 = eFrom.size();
        var size2 = eTo.size();
        ctx.lineWidth = 0.5+u5[i]*500;
        ctx.beginPath();
        ctx.moveTo(pos1.left + eFrom.width() + 3, pos1.top + eFrom.height() / 2);
        ctx.lineTo(pos2.left + 5, pos2.top + eTo.height() / 2);
        ctx.stroke();

    }
}
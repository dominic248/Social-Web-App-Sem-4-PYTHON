document.getElementById("content").style.visibility = "hidden";

document.getElementById("outercontent").onmouseenter = function() {mouseEnter()};
document.getElementById("outercontent").onmouseleave = function() {mouseLeave()};

function mouseEnter() {
    document.getElementById("content").style.visibility = "visible";
}
function mouseLeave() {
    document.getElementById("content").style.visibility = "hidden";
}

var notIE = (document.documentMode === undefined),
isChromium = window.chrome;
if (notIE && !isChromium) {
    // checks for Firefox and other  NON IE Chrome versions
    $(window).on("focusin", function () {
        // tween resume() code goes here
        setTimeout(function(){
            console.log("focus");
            mouseEnter();
        },10);
    }).on("focusout", function () {
        // tween pause() code goes here
        console.log("blur");
        mouseLeave();
    });
} else {
    // checks for IE and Chromium versions
    if (window.addEventListener) {
        // bind focus event
        window.addEventListener("focus", function (event) {
            // tween resume() code goes here
            setTimeout(function(){
                console.log("focus");
                mouseEnter();
            },10);
        }, false);
        // bind blur event
        window.addEventListener("blur", function (event) {
            // tween pause() code goes here
            console.log("blur");
            mouseLeave();
        }, false);
    } else {
        // bind focus event
        window.attachEvent("focus", function (event) {
            // tween resume() code goes here
            setTimeout(function(){
                console.log("focus");
                mouseEnter();
            },10);
        });
        // bind focus event
        window.attachEvent("blur", function (event) {
            // tween pause() code goes here
            console.log("blur");
            mouseLeave();
        });
    }
}
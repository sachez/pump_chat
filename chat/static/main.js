$(document).ready(function(){
   $("#add").click(function() {
       var key = $("#currency").val();
       if(document.getElementById(key) === null) {
           var $div = $("<div class=\"col\" id=\"" +
               key +
               "\">" +
               key +
               ":" +
               localStorage.getItem(key) +
               "</div>"
           );
           $("#list").append($div);
       }
   })

});

function setupWebSocket() {
    var wsaddr = window.location.host;
    var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
    var path = window.location.pathname.replace(/\/$/, "");
    var wsUri = ws_scheme + "://" + wsaddr + path + "/ws/";
    var websocket = new WebSocket(wsUri);
    websocket.onopen = function (evt) {
        onOpen(evt);
    }
    websocket.onmessage=function(evt){
        onMessage(evt);
    }
    websocket.onclose=function(evt){
        onClose(evt);
    }
}

function onMessage(evt){
    var json_curse = JSON.parse(evt['data']);
    var options = new Array();
    var option;
    for(var key in json_curse){
        option = document.createElement('option');
        option.text = key;
        options.push(option);
    }
    $('#currency').append(options);
    localStorage.setItem('curse', json_curse);

    var list = document.getElementById("list").children;
    var l = list.length;
    for(var i = 0; i < l; ++i){
        var node = list[i];
        if(json_curse.hasOwnProperty(node.id) === true){
            node.textContent = node.id + ": " + json_curse[node.id];
        }
    }
}

function onOpen(evt){
    console.log("Web Socket connection establish.");
}

function onClose(evt) {
    console.log("WebSocket is close!");
}

$(window).on('load', setupWebSocket);


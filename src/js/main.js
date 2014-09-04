$("#convert").click(function(event){
    xmlConvert()
});

function xmlConvert(){
    originalText = document.getElementById("input").value
    console.log(originalText)
    data={"data": originalText}
    $.ajax({
        type: "GET",
        url: "/api/xml",
        data: JSON.stringify( data ),
        contentType: "application/json; charset=utf-8",
        success: function(data){
            console.log(data)
            displayResult(data);
        },
        failure: function(err) {
            alert(err);
        }
    }); 
}

function displayResult(data){
    //Clean up
    $("#output").val("")
    $("#output").val(data)
}



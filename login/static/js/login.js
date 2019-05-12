$(document).ready(function(){
    $('#go').click(function(){
        let id=$('#ident').val();
        let pass=$('#pass').val();
        $.ajax({
            url:"http://127.0.0.1:8000/verifData/",
            type:"POST",
            data: "id="+id+"&password="+pass,
            dataType:'text',
            success:function(code){
                console.log(code);
                $( location ).attr("href", "http://127.0.0.1:8000/vendeur/accueil/");
            },
            error:function(result,statut,error){
                console.log(error);
                
            }
            
        });

    });
});

var produits=[
    {produit:'mango',quantite:2,prix:2000,remise:10,prixT:4000,t:20000},
    {produit:'mango',quantite:2,prix:2000,remise:10,prixT:4000,t:20000},
    {produit:'mango',quantite:2,prix:2000,remise:10,prixT:4000,t:20000},
];
createList();
function remise(){
    document.getElementById('r').style.display=document.getElementById('r').style.display=="none"?"":"none";
}
function createList(){
    
    var mag=produits.map(p =>{
        document.createElement('option').setAttribute('value',p.produit);
    });
    document.getElementById('listeProduits').innerHTML=mag;
}
function addProduct(){
    var t="";
    
    for(let i=0;i<produits.length;i++){
        //705651426
        let tab=document.createElement('tr');
        let td1=document.createElement('td');
        td1.innerText=produits[i].produit;
        tab.appendChild(td1);
        let td2=document.createElement('td');
        td2.innerText=produits[i].quantite;
        tab.appendChild(td2);
        let td3=document.createElement('td');
        td3.innerText=produits[i].prix;
        tab.appendChild(td3);
        let td4=document.createElement('td');
        td4.innerText=produits[i].remise;
        tab.appendChild(td4);
        let td5=document.createElement('td');
        td5.innerText=produits[i].prix;
        tab.appendChild(td5);
        let td6=document.createElement('td');
        td6.innerText=produits[i].t;
        tab.appendChild(td6);
        let btn=document.createElement('input');
        btn.setAttribute('type','button');
        btn.setAttribute('value','supprimer');
        btn.setAttribute('class','btn btn-danger');
        let td7=document.createElement('td');
        td7.appendChild(btn);
        tab.appendChild(td7);
        document.getElementById('tabid').appendChild(tab);
    }
}
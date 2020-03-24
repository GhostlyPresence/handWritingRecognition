

window.addEventListener("load",()=>
{
    const canvas = document.querySelector('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 500;
    canvas.height = 500;
    let mx=700;
    let my=20;

    


    const sendBtn = document.getElementById("predict")
    const clrBtn = document.getElementById("clear")

    let painting = false;
    function startPos(e)
    {
        painting = true;
        draw(e);
    }

    function finPos()
    {
        painting = false;
        ctx.beginPath();
    }

    function draw(e){
        if(!painting) return;
   
        ctx.lineWidth=40;
        ctx.lineCap="round";
        
        ctx.strokeStyle = "rgba(255,255,255,1)";
        ctx.lineTo(e.clientX-mx,e.clientY-my);
        ctx.stroke();

    }

    //event listeners
    canvas.addEventListener("mousedown",startPos);
    canvas.addEventListener("mouseup",finPos);
    canvas.addEventListener("mousemove",draw);

    sendBtn.addEventListener("click",function ()
    {
        
       /* const a = document.createElement("a");
        document.body.appendChild(a);*/
        const dataURI = canvas.toDataURL();

        let data = {image : dataURI}
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function(){
            if(xhr.readyState === 4){
                res = xhr.response;
                if(res =='0')
                {
                    document.getElementById('output').value = "Please Enter A valid number..I'm an AI not human";
                }
                else{
                    document.getElementById('output').value = "The result is " + res;
                }
                
                console.log(res);


            }
        }
        xhr.open("POST","/",true);
        xhr.send(JSON.stringify(data))


    });
    clrBtn.addEventListener("click",function(){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        document.getElementById('output').value = "Draw a number";
    })

});
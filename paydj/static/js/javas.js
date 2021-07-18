
console.log("java is on ")
const buttons =  document.querySelectorAll('.ripple');


buttons.forEach(button =>
    {
        button.addEventListener('click',function(e)
        {
            // acc.to viewport
            const x = e.clientX; 
            const y = e.clientY;
        
            // position of button element in the body
            const buttonleft = e.target.offsetLeft;
            const buttontop = e.target.offsetTop;
        
            // clicked position wrt to button only
            const xInside = x - buttonleft;
            const yInside = y - buttontop;

            // console.log(xInside,yInside);

            const ele = document.createElement('span')
            ele.className = 'circle';
            ele.style.left = xInside + 'px';
            ele.style.top = yInside + 'px';
            button.appendChild(ele);
        
    })


})


// // type writer text
// var i = 0,text;
// text = "Welcome to Sparks Foundation"

// function typing()
// {
//     if(i<text.length)
//     {
//         document.getElementById("text") += text.charAt(i);
//         i++;
//         setTimeout(typing,50);
//     }
    
// }
// typing();

// ALERT
const notstart = document.getElementsByClassName('notstart');
console.log(notstart)

Array.from(notstart).forEach(function(e)
{

    e.addEventListener('click',()=>{
    
        alert("Login to donate!!");
    })
})


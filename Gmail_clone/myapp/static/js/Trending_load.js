let container = document.getElementById('carousel-inner-container')

// static/myapp/js/sc.js
document.addEventListener('DOMContentLoaded', function () {
    fetch('/static/Reload_dataset/trending_games.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            let carouselItem = ''
            data.map((item,index) => {
                
                 carouselItem += `
                  <div class="carousel-item ${index === 0 ? 'active' : ''}" data-bs-interval="2000">
                  
                   <img src="${item.Img}" class="Home-image d-block w-100" alt="..."> 
                 
                   <div class="carousel-caption d-none d-md-block">
                    <h2>${item.Title}</h2>
                     <p>${item.desc}</p>
                      <p>${item.Release_date}</p>
                       </div> 
                       </div> `;
                       

        })
        
    container.innerHTML=carouselItem;
        
    },
    
)
    
    
});


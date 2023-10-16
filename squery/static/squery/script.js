document.addEventListener("DOMContentLoaded", function () {

    const message_sec = document.querySelector('.messages');
    
    if(message_sec){
        setTimeout(function() {
            message_sec.style.display = 'none';
        }, 5000);
    }


// const voteButtons = document.querySelectorAll('.vote-button');

// // Iterate through the buttons and attach the event handler to each
// voteButtons.forEach(function(button) {
//   button.addEventListener('click', function(e) {
//     e.preventDefault();
    
//     // Get the post ID from the data attribute
//     const id = this.getAttribute('data-post-id');

//     // Rest of your code (e.g., changing the vote status and fill color)

//     let vote = this.getAttribute('data-vote');

//     if (vote === 'vote') {
//         vote = 'voted';
//         this.classList.add('voted');
//         this.setAttribute('data-vote', 'voted');
//       } else {
//         vote = 'vote';
//         this.setAttribute('data-vote', 'vote');
//         this.classList.remove('voted');
//       }
    
//     // Use 'id' here to identify the post
//     console.log('Clicked on post with ID:', id);

//   });
// });


    // Admin settings
    const info_btn = document.querySelector('.btn-inf');
    const info_section = document.querySelector('.name-section'); 
    const query_btn = document.querySelector('.btn-dashboard');
    const query_sec = document.querySelector('.admin-dashsec');

    info_btn.addEventListener("click", function(e){
        e.preventDefault();
        console.log(info_section.style.display);
        // info_section.style.display="block";
        if (info_section.style.display === 'none'){
            query_sec.style.display = "none"
            info_section.style.display="block";

        }else{
            info_section.style.display="none";
        }
    });
    query_btn.addEventListener("click", function(e) {
        e.preventDefault();
        query_sec.style.display = "block";
        info_section.style.display = "none";
    });
    
});

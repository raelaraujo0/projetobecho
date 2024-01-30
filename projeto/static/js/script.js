function toggleSidebar(){
    var sidebar = document.querySelector('.sidebar')

    if(sidebar.style.left == '-200px'){
        sidebar.style.left = '0';
        sidebar.style.marginLeft = '200px';
        document.querySelector('. flecha img').style.transform = 'rotate(0deg)';
    } else {
        sidebar.style.left = '200px';
        sidebar.style.marginLeft = '20px';
        document.querySelector('. flecha img').style.transform = 'rotate(180deg)';
    }
}
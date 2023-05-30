document.addEventListener("DOMContentLoaded", function () {
    const loader = document.getElementById("loader");
    loader.style.display = "none";


    // fix form profil for avatar
    const linkAvatar = document.querySelector("tr.input-avatar > td > a");
    if (linkAvatar) {
        linkAvatar.insertAdjacentHTML("afterend", "</br>");
        console.log("linkAvatar");
        linkAvatar.setAttribute("target", "_blank");
    }
});


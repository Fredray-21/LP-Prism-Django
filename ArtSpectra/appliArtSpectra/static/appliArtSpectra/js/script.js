document.addEventListener("DOMContentLoaded", function () {
    const loader = document.getElementById("loader");
    loader.style.display = "none";


    // fix form profil for avatar
    const linkAvatar = document.querySelector("tr.input-avatar > td > a");
    if (linkAvatar) {
        linkAvatar.insertAdjacentHTML("afterend", "</br>");
        linkAvatar.setAttribute("target", "_blank");
    }

    // remove du label et du checkbox pour supprimer l'image de l'oeuvre
    const checkboxDelOeuvre = document.querySelector("#imageOeuvre-clear_id");
    const LabelcheckboxDelOeuvre = document.querySelector(`label[for="imageOeuvre-clear_id"]`);

    checkboxDelOeuvre && checkboxDelOeuvre.remove();
    LabelcheckboxDelOeuvre && LabelcheckboxDelOeuvre.remove();
});


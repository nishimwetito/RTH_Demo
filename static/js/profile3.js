let liked = false;

function toggleLike() {
    let heartIcon = document.getElementById("heartIcon-3");
    let likeCount = document.getElementById("likeCount-3");

    if (!liked) {
        heartIcon.classList.remove("far");
        heartIcon.classList.add("fas");
        heartIcon.style.color = "#e63946";
        likeCount.innerText = "1.3k Likes";
    } else {
        heartIcon.classList.remove("fas");
        heartIcon.classList.add("far");
        heartIcon.style.color = "#e76f51";
        likeCount.innerText = "1.2k Likes";
    }
    liked = !liked;
}
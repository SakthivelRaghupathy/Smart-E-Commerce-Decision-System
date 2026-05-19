function showNotification(message, type = "success") {

    const notification = document.createElement("div");
    notification.className = `notification ${type}`;
    notification.innerText = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add("hide");
    }, 2000);

    setTimeout(() => {
        notification.remove();
    }, 2500);
}
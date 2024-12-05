function expandImage(img) {
  const modal = document.getElementById("modal");
  const modalImage = document.getElementById("modal-image");

  modal.style.display = "block";
      
  modalImage.style.position = "fixed";
  modalImage.style.top = "50%";
  modalImage.style.left = "50%";
  modalImage.style.transform = "translate(-50%, -50%)";
  

  modalImage.style.width = "auto";
  modalImage.style.height = "auto"; 
  modalImage.style.border = "none";
  modalImage.src = img.src;    
  
  modal.addEventListener("click", function(event) {
    if (event.target === modal) {
      closeModal();
    }
  });
}
  
function closeModal() {
  const modal = document.getElementById("modal");
  modal.style.display = "none";
}

;(function () {
  const toastElement = document.getElementById("toast")
  const toastBody = document.getElementById("toast-body")
  const toast = new bootstrap.Toast(toastElement, {
    delay: 2000,
    animation: true,

  })



  htmx.on("showMessage", (e) => {

    toastBody.innerText = e.detail.value
    toast.show()


  })
})()
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-complete-url]").forEach((button) => {
    button.addEventListener("click", async () => {
      button.disabled = true;
      button.innerHTML = "写入学习记录…";
      const response = await fetch(button.dataset.completeUrl, {
        method: "POST",
        headers: { "X-CSRFToken": getCookie("csrftoken") },
      });
      if (response.ok) {
        window.location.reload();
      } else {
        button.disabled = false;
        button.innerHTML = "标记为已完成 <span>✓</span>";
      }
    });
  });

  document.querySelectorAll("[data-copy-target]").forEach((button) => {
    button.addEventListener("click", async () => {
      const target = document.getElementById(button.dataset.copyTarget);
      await navigator.clipboard.writeText(target.innerText);
      const original = button.innerText;
      button.innerText = "已复制";
      setTimeout(() => { button.innerText = original; }, 1300);
    });
  });
});

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
  return "";
}

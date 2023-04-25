(function() {
  // Add an event listener to the delete form to handle the AJAX request
  const deleteForms = document.querySelectorAll('form[method="POST"][hx-delete]');
  deleteForms.forEach(form => {
    form.addEventListener('htmx:beforeSend', () => {
      // Disable the delete button while the request is being processed
      const deleteButton = form.querySelector('button[type="submit"]');
      deleteButton.disabled = true;
    });
    form.addEventListener('htmx:afterSwap', () => {
      // Enable the delete button after the request has completed
      const deleteButton = form.querySelector('button[type="submit"]');
      deleteButton.disabled = false;
    });
    form.addEventListener('htmx:afterRequest', () => {
      // Replace the todo list container with the updated HTML
      const todoContainer = document.querySelector('#todo-container');
      todoContainer.outerHTML = this.response;
    });
  });
})();
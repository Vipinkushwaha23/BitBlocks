document.getElementById('billingToggle').addEventListener('change', function() {
    if (this.checked) {
        // Billed yearly (discounted price)
        document.getElementById('price-startup').textContent = '12';
        document.getElementById('price-business').textContent = '24';
        document.getElementById('price-agency').textContent = '120';
    } else {
        // Billed monthly (regular price)
        document.getElementById('price-startup').textContent = '14';
        document.getElementById('price-business').textContent = '29';
        document.getElementById('price-agency').textContent = '139';
    }
});

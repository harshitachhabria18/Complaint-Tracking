document.getElementById('filterForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const status = this.elements.status.value;
    const category = this.elements.category.value;
    const dateRange = this.elements.dateRange.value;

    const rows = document.querySelectorAll('#complaintsTable tbody tr');
    rows.forEach(row => {
        let show = true;

        if (status && row.dataset.status !== status) show = false;
        if (category && row.dataset.category !== category) show = false;
        if (dateRange) {
            const days = parseInt(dateRange);
            const complaintDate = new Date(row.dataset.date);
            const cutoff = new Date();
            cutoff.setDate(cutoff.getDate() - days);
            if (complaintDate < cutoff) show = false;
        }

        row.style.display = show ? '' : 'none';
    });
});

document.getElementById('resetFilters').addEventListener('click', () => {
    document.getElementById('filterForm').reset();
    document.querySelectorAll('#complaintsTable tbody tr').forEach(r => r.style.display = '');
});


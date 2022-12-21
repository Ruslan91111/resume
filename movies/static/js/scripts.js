const rate = (rating, movies_id) => {
    fetch(`/rate/${movies_id}/${rating}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(rest => {
        window.location.reload();
        // you may want to update the rating here
        // to simplify stuff, I just reload the page
    })
}
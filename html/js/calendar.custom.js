function fetchData() {
    return fetch(`calendar.json`)
        .then(result => result.json())
        .then(result => {
            if (result) {
                return result.map(r => ({
                    startDate: new Date(r.startDate),
                    endDate: new Date(r.startDate),
                    name: r.name,
                    linkId: r.id,
                    color: '#037a33'
                }));
            }
            return [];
        });
}


const calendar = new Calendar('#calendar', {
    startYear: 1888,
    language: "de",
    dataSource: fetchData,
    clickDay: function (e) {
        console.log(e.events[0].linkId);
        window.location = e.events[0].linkId;
    },
});
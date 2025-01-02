const form = document.querySelector('#profile-form')

async function postProfile() {
	form_data = new FormData(form);
	var data = Object.fromEntries(form_data);
	data.age = Number(data.age);

	try {
		const response = await fetch('/profiles/post-profile', {
			method: 'POST',
			headers: {
				"Content-Type": "application/json; charset=utf-8"
			},
			body: JSON.stringify(data),
		});
		console.log(await response.json());
	} catch (e) {
		console.error(e);
	}
}

form.addEventListener('submit', (event) => {
	event.preventDefault();
	postProfile();
	form.reset();
});

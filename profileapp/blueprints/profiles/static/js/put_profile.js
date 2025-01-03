const form = document.querySelector('#profile-update-form')

async function updateProfile() {
	const form_data = new FormData(form);
	var data = Object.fromEntries(form_data);
	data.pid = Number(data.pid);
	data.age = Number(data.age);

	try {
		const response = await fetch('/profiles/put-profile', {
			method: 'PUT',
			headers: {
				"Content-Type": "application/json; charset=utf-8"
			},
			body: JSON.stringify(data),
		});
		console.log(await response.json());
	} catch (e) {
		console.error(e);
	}

	window.location.replace('/profiles');
}


form.addEventListener('submit', (event) => {
	event.preventDefault();
	updateProfile();
});

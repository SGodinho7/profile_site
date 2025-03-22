const form = document.querySelector('#profile-update-form');

async function updateProfile() {
	const form_data = new FormData(form);

	try {
		const response = await fetch('/profiles/put-profile', {
			method: 'PUT',
			body: form_data,
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

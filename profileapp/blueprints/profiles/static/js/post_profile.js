const form = document.querySelector('#profile-form')

async function postProfile() {
	form_data = new FormData(form);

	try {
		const response = await fetch('/profiles/post-profile', {
			method: 'POST',
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
	postProfile();
});

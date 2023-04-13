const saveForm = document.getElementById('form')
const charCount = document.getElementById('char-count')
const textContent = document.getElementById('text')

textContent.addEventListener('input', () => {
    charCount.textContent = textContent.value.length
})

saveForm.addEventListener('sumbit', async (event) => {
    event?.preventDefault();

    const form = new FormData(saveForm)
    const response = await fetch('/api/texts/', {
        method: 'POST',
        body: form,
    })
    const data = await response.json()
    return data
})
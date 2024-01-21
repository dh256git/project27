  const handleChange = (select) => {
    const option = select.selectedOptions[0];

    const value = option.value;
    const label = option.label;
    const text = option.text;


    console.log(value, label, text);

    document.getElementById('iframe-id').setAttribute('src', value);
    document.getElementById('iframe-id').setAttribute('title', label);
        document.getElementById('team-members').innerHTML = null;
        document.getElementById('team-members').innerHTML = text;
  }

  const handleChange2 = (select) => {
    const option = select.selectedOptions[0];

    const value = option.value;
    const label = option.label;
    const text = option.text;

    console.log(value, label, text);

    document.getElementById('iframe-id2').setAttribute('src', value);
    document.getElementById('iframe-id2').setAttribute('title', label);
        document.getElementById('frame-heading').innerHTML = text;
  }

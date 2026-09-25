// ServiceNow Client Script | Type: onSubmit | Table: Incident
function onSubmit() {
    if (g_form.getValue('caller_id') == '') { g_form.addErrorMessage('Caller is required.'); return false; }
    if (g_form.getValue('description') == '') { g_form.addErrorMessage('Description is required.'); return false; }
    return true;
}

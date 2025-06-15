function doPost(e) {
  const sheet = SpreadsheetApp.openById('<<スプレッドシートID>>').getSheetByName('<<シート名>>');
  const data = JSON.parse(e.postData.contents);

  sheet.appendRow([
    new Date(),
    data.userName || '',
    data.soulType || '',
    data.answer1 || '',
    data.answer2 || '',
    data.answer3 || ''
  ]);

  return ContentService.createTextOutput("OK");
}

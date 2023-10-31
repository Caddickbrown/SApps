- [ ] Remove Filesaver requirement

To remove the dependency on FileSaver.js while maintaining the same functionality for saving files, you can use the built-in File System Access API, which is supported in modern browsers. This API allows you to prompt the user to save files directly to their local file system without the need for an external library like FileSaver.js.

Here’s how you can modify your code to use the File System Access API:

1. Remove the script tag that loads FileSaver.js from your HTML file.

2. Replace the `saveBlob` function with a new function that uses the File System Access API to save the file:

```javascript
async function saveFile(filename, data, type) {
  try {
    const handle = await window.showSaveFilePicker({
      suggestedName: filename,
      types: [
        {
          description: ‘Files’,
          accept: {
            [type]: [‘.’]
          }
        }
      ]
    });
    const writable = await handle.createWritable();
    await writable.write(data);
    await writable.close();
  } catch (error) {
    console.error(‘Unable to save file:’, error);
  }
}
```

3. Modify the `exportAsMarkdown`, `exportAsCSV`, and other export functions to use the `saveFile` function:

```javascript
function exportAsMarkdown() {
  const { date, title, journal } = getFormData();
  const tags = getTagsString();
  const markdownData = `# ${date}\n## ${title}\n\n${tags}\n\n—\n${journal}\n`;
  const filename = getFilename(‘md’);
  saveFile(filename, markdownData, ‘text/markdown’);
}

function exportAsCSV() {
  const { date, title, tags, journal } = getFormDataWithTags();
  const csvData = `”Date”,”Title”,”Tags”,”Journal Entry”\n”${date}”,”${title}”,”${tags}”,”${journal}”`;
  const filename = getFilename(‘csv’);
  saveFile(filename, csvData, ‘text/csv’);
}

function exportAsJSON() {
  const formData = getFormDataWithTags();
  const jsonData = JSON.stringify(formData, null, 2);
  const filename = getFilename(‘json’);
  saveFile(filename, jsonData, ‘application/json’);
}
```

4. Make sure to update the `submitTag` function as well if it uses `saveBlob`.

With these changes, you’ll be using the File System Access API to prompt the user to save files directly without the need for the FileSaver.js library. Keep in mind that the File System Access API is a modern API, so it may not be supported in all browsers. Make sure to check the browser compatibility before deploying your application. Additionally, as the API is asynchronous, ensure that you handle errors appropriately and provide fallback options for older browsers that do not support the API.

- [ ] Add methodology to README
- [ ] Reading Mode? How would this work?





Introducing Journaller - Your Private, Offline-Friendly Journaling App

Welcome to Journaller, your ultimate privacy-focused journaling app designed to keep your thoughts secure, accessible offline, and free from the cloud. With Journaller, you can seamlessly record your daily musings, memorable moments, and reflections in a single HTML-based page that can be stored on a USB drive. No need to worry about your personal data being stored on external servers - it’s all kept within your reach.

Methodology:

1. Simple and Seamless: Journaller offers a straightforward user interface, making journaling a breeze. Write your entries, save, and export with ease.

2. Offline Accessibility: Say goodbye to relying on an internet connection. Journaller works entirely offline, ensuring your writing remains accessible wherever you go.

3. Export Versatility: Journaller empowers you to export your journal entries to various formats like markdown, ensuring compatibility with other tools and platforms.

4. USB Storage: All your exported files are securely stored on the same USB drive as your Journaller page. This way, you retain full control over your data without entrusting it to cloud services.

5. Privacy-Focused: At Journaller, we understand the importance of privacy. Your data is kept locally, safeguarding it from prying eyes and potential security breaches.

6. Free and Open Source: We believe in open-source principles, making Journaller accessible to all, without any cost. You’re free to customize and enhance the app to suit your specific needs.

Begin your journaling journey with Journaller and experience the freedom of expressing yourself without compromising on privacy. Your thoughts are valuable and deserve a secure space to flourish. Let Journaller be your trusted companion in capturing life’s beautiful moments. Happy journaling!



Using an HTML file for a journaling app like Journaller offers several advantages over connecting to the internet:

1. Offline Accessibility: Since Journaller is an HTML-based app, it functions entirely offline. You don’t need an internet connection to write, read, or access your journal entries. This is particularly beneficial when you want to write in remote or offline areas, such as during travels or in places with limited connectivity.

2. Privacy and Security: By keeping your journal data on a local HTML file and a USB drive, you have complete control over your information. There’s no risk of your personal thoughts being stored on external servers or cloud platforms, reducing the chances of unauthorized access or data breaches.

3. Portability: Storing your journal entries in a single HTML file that can be saved on a USB drive makes it highly portable. You can carry your journal with you wherever you go, ensuring it’s accessible across different devices without the need for an internet connection.

4. Independence from Cloud Services: Some people prefer not to rely on cloud services for storing sensitive and private information, as it may raise concerns about data ownership, data mining, or unwanted surveillance. Using an HTML file on a USB drive grants you complete independence from cloud storage, providing peace of mind regarding your data’s security and privacy.

5. Platform Agnostic: HTML files are compatible with various operating systems and devices, making Journaller versatile and accessible across different platforms. Whether you use Windows, macOS, Linux, or other operating systems, you can access your journal with ease.

6. Customization and Control: Since Journaller is free and open source, you can modify the app according to your preferences and needs. You have full control over how your journaling experience looks and feels, empowering you to create a personalized space for your thoughts.

In summary, using an HTML file for Journaller offers users the benefits of offline access, enhanced privacy, portability, platform agnosticism, and the ability to customize the app to suit individual requirements. It caters to users who prioritize privacy-focused, offline-friendly journaling without relying on internet-based services.


Having Journaller as a fully self-contained application offers several significant benefits:

1. **No External Dependencies:** Since Journaller is self-contained, it doesn’t rely on external dependencies or additional software installations. Users can run the app directly from the USB drive without the need to install anything on the host computer. This makes it convenient and hassle-free, particularly when using public or shared computers where installing software may not be allowed.

2. **Portability:** The self-contained nature of Journaller ensures high portability. You can carry the entire app, including your journal entries, on a USB drive, allowing you to access it on multiple devices without leaving any traces on the host computers. It’s like carrying your personal journaling app in your pocket.

3. **Offline Accessibility:** As an entirely self-contained app, Journaller works offline without relying on an internet connection or cloud services. You can write, edit, and export journal entries even in places without internet access, making it ideal for travelers, remote locations, or situations with limited connectivity.

4. **Security and Privacy:** Since Journaller operates independently from the host computer’s operating system and doesn’t leave any data behind, it enhances security and privacy. There’s no risk of leaving traces of your personal information on public computers or compromising your data’s confidentiality.

5. **Data Ownership:** With Journaller being self-contained, you retain full ownership and control over your journal entries. Your data remains with you on the USB drive, and you can choose to keep it entirely private without sharing it with external services.

6. **Cross-Platform Compatibility:** The self-contained nature of Journaller ensures compatibility across different operating systems and devices. You can use it on Windows, macOS, Linux, or any other platform without the need for platform-specific versions.

7. **Easy Backups and Migration:** Since all your data is stored on the USB drive, it becomes straightforward to create backups by duplicating the drive. Additionally, if you want to switch to a new device or computer, you can easily migrate your journaling app along with all your entries by transferring the USB drive.

In summary, the self-contained nature of Journaller offers users the advantages of no external dependencies, high portability, offline accessibility, enhanced security, data ownership, cross-platform compatibility, and simplified backups and migration. It ensures a seamless and private journaling experience wherever you go, without leaving any trace on the host system.



The interoperability of standards like Markdown, CSV (Comma-Separated Values), and JSON (JavaScript Object Notation) in Journaller provides significant usefulness and flexibility to users:

1. **Data Portability:** By supporting these interoperable standards, Journaller allows users to export their journal entries into different formats. For instance, converting your journal entry to Markdown enables easy integration with various text editors and publishing platforms, making it simple to share or cross-reference your writing in other environments.

2. **Cross-Platform Compatibility:** Markdown, CSV, and JSON are widely supported across various platforms and applications. Journaller’s ability to export to these formats allows users to access their journal entries seamlessly on different devices, operating systems, and software without compatibility issues.

3. **Backup and Migration:** Interoperable standards facilitate easy backup and migration of data. You can store your journal entries in multiple formats on your USB drive, ensuring redundancy and quick retrieval in case of any data loss or device change.

4. **Integration with Third-Party Tools:** Exporting journal entries in these formats enables integration with a wide range of third-party tools and services. For instance, you can use CSV exports for data analysis or JSON for integration with other apps and platforms.

5. **Long-Term Data Preservation:** These interoperable standards ensure long-term data preservation. As these formats have widespread adoption and are less prone to obsolescence, your journal entries remain accessible and readable for years to come.

6. **Customization and Adaptability:** Users can leverage the flexibility of these standards to customize and adapt their journal entries for specific needs. For example, you can import your CSV data into a spreadsheet application and manipulate it to create personalized reports or summaries of your journaling history.

7. **Community Support:** Being widely used and recognized, Markdown, CSV, and JSON have active communities that develop and support various tools and libraries. This means that you can find a wealth of resources, plugins, and software to enhance your journaling experience.

In summary, the interoperability of Markdown, CSV, and JSON in Journaller offers users data portability, cross-platform compatibility, backup and migration options, integration with third-party tools, long-term data preservation, customization opportunities, and access to thriving communities for ongoing support and innovation. This ensures a versatile and future-proof journaling experience, catering to various user preferences and requirements.
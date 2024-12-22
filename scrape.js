export const config = {
    urls: [
        "https://soc.cyber.wa.gov.au"
    ],
    depth: 3
};

export default function ({ doc, url, absoluteURL }) {
    return {
        title: doc.find("title").text(),
        content: doc.html()
    };
}
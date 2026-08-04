import dayjs from "dayjs";

console.log("Current Date: ",dayjs().format());
//frappe.show_alert("Welcome!");
frappe.router.on("change", () => {
    setTimeout(() => {
        $(".list-liked-by-me").hide();
        $(".like-action").hide();
    }, 100);
});
/**frappe.listview_settings["Student"] = {
	onload(listview) {
		listview.$page.find(".list-liked-by-me").hide();
	},
	refresh(listview) {
		listview.$page.find(".list-liked-by-me").hide();
		listview.$page.find(".like-action").hide();
	},
};**/
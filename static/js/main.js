const mobileMenuBtn =
    document.getElementById("mobileMenuBtn");

const mainNav =
    document.getElementById("mainNav");


if (mobileMenuBtn && mainNav) {

    mobileMenuBtn.addEventListener(
        "click",
        () => {

            mainNav.classList.toggle("active");

        }
    );


    const navLinks =
        mainNav.querySelectorAll("a");


    navLinks.forEach(
        link => {

            link.addEventListener(
                "click",
                () => {

                    mainNav.classList.remove(
                        "active"
                    );

                }
            );

        }
    );

}
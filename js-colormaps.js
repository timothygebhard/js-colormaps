function raw_to_rgb(r_raw, g_raw, b_raw) {

    // Takes values for red, green and blue in [0, 1] and returns the tuple
    // (r, g, b) with r, g, b in [0, 255]

    var r = Math.max(0, Math.round(255 * r_raw));
    var g = Math.max(0, Math.round(255 * g_raw));
    var b = Math.max(0, Math.round(255 * b_raw));

    return [r, g, b];
}



function option_a(x) {

    var r_raw =  0.012152 * Math.pow(x, 0) + -0.590007 * Math.pow(x, 1) +  19.877737 * Math.pow(x, 2) + -92.1863860 * Math.pow(x, 3) +  230.212147 * Math.pow(x, 4) + -307.563475 * Math.pow(x, 5) +  204.252541 * Math.pow(x, 6) + -53.025213 * Math.pow(x, 7);
    var g_raw = -0.025537 * Math.pow(x, 0) +  2.163341 * Math.pow(x, 1) + -23.749618 * Math.pow(x, 2) +  127.011068 * Math.pow(x, 3) + -339.098404 * Math.pow(x, 4) +  477.858564 * Math.pow(x, 5) + -335.833172 * Math.pow(x, 6) +  92.669465 * Math.pow(x, 7);
    var b_raw =  0.011971 * Math.pow(x, 0) +  1.223241 * Math.pow(x, 1) +  17.781960 * Math.pow(x, 2) + -111.293799 * Math.pow(x, 3) +  282.338892 * Math.pow(x, 4) + -384.392951 * Math.pow(x, 5) +  275.309006 * Math.pow(x, 6) + -80.251369 * Math.pow(x, 7);

    return raw_to_rgb(r_raw, g_raw, b_raw);

}



function option_d(x) {

    var r_raw =  0.256624 * Math.pow(x, 0) +  1.161777 * Math.pow(x, 1) + -14.789418 * Math.pow(x, 2) +  76.314489 * Math.pow(x, 3) + -217.079892 * Math.pow(x, 4) +  326.813590 * Math.pow(x, 5) + -238.180434 * Math.pow(x, 6) +  66.499533 * Math.pow(x, 7);
    var g_raw =  0.003955 * Math.pow(x, 0) +  1.503667 * Math.pow(x, 1) + -1.2559730 * Math.pow(x, 2) +  2.4706350 * Math.pow(x, 3) + -8.55355200 * Math.pow(x, 4) +  19.0035210 * Math.pow(x, 5) + -19.0283440 * Math.pow(x, 6) +  6.7628160 * Math.pow(x, 7);
    var b_raw =  0.322928 * Math.pow(x, 0) +  1.962267 * Math.pow(x, 1) + -7.8040080 * Math.pow(x, 2) +  24.885368 * Math.pow(x, 3) + -65.2506820 * Math.pow(x, 4) +  110.516218 * Math.pow(x, 5) + -100.802275 * Math.pow(x, 6) +  36.306961 * Math.pow(x, 7);

    return raw_to_rgb(r_raw, g_raw, b_raw);

}


function Greens(x) {

    var r_raw =  0.964649 * Math.pow(x, 0) +  -0.183278 * Math.pow(x, 1) + -5.436727 * Math.pow(x, 2) +  27.653655 * Math.pow(x, 3) + -88.568240 * Math.pow(x, 4) + 144.388549 * Math.pow(x, 5) + -113.084088 * Math.pow(x, 6) +  34.278302 * Math.pow(x, 7); 
    var g_raw =  0.987456 * Math.pow(x, 0) +  -0.156843 * Math.pow(x, 1) + -0.380759 * Math.pow(x, 2) + -2.2022450 * Math.pow(x, 3) +  9.7346650 * Math.pow(x, 4) + -19.765903 * Math.pow(x, 5) +   18.512335 * Math.pow(x, 6) +  -6.468158 * Math.pow(x, 7);
    var b_raw =  0.963022 * Math.pow(x, 0) +  -0.767257 * Math.pow(x, 1) +  2.560923 * Math.pow(x, 2) + -22.400962 * Math.pow(x, 3) +  59.633418 * Math.pow(x, 4) + -71.403993 * Math.pow(x, 5) +   39.539013 * Math.pow(x, 6) +  -8.014166 * Math.pow(x, 7);
    
    return raw_to_rgb(r_raw, g_raw, b_raw);

}
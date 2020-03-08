/* See https://github.com/MichMich/MagicMirror#configuration */

// START -- DIGITAL CLOCK --
const digital_clock = [
    {
        module: "clock",
        position: "middle_center",
        classes: "clock-time-only",
        config: {
            displaySeconds: false,
            showDate: false
        }
    },
]
// END -- DIGITAL CLOCK --

// START -- Calendar Day --
const digital_clock_date = [
    {
        module: "clock",
        position: "middle_center",
        classes: "clock-date-only",
        config: {
            displaySeconds: false
        }
    },
]
// END -- Calendar Day --

// START -- IP --
const ip = [
    {
        module: 'MMM-ip',
        position: 'bottom_right',
        config: {
            showFamily: "IPv4",
            showType: "both",
            voice: false
        }
    }
];
// END -- IP --

var config = {
  address: "0.0.0.0", // Address to listen on, can be:
  // - "localhost", "127.0.0.1", "::1" to listen on loopback interface
  // - another specific IPv4/6 to listen on a specific interface
  // - "", "0.0.0.0", "::" to listen on any interface
  // Default, when address config is left out, is "localhost"
  port: 8080,
  ipWhitelist: [], // Set [] to allow all IP addresses
  // or add a specific IPv4 of 192.168.1.5 :
  // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
  // or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
  // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

  language: "sv",
  timeFormat: 24,
  units: "metric",

  modules: [
    ...digital_clock,
    ...digital_clock_date,
    ...ip
  ]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {
  module.exports = config;
}

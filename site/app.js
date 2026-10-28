const entrance = document.querySelector('#entrance');
const status = document.querySelector('#entrance-status');
const lights = [...document.querySelectorAll('.start-lights span')];
const skip = document.querySelector('#skip-entrance');

function openArchive() {
  entrance.classList.add('open');
  document.body.classList.add('entered');
}

let lightIndex = 0;
const lightTimer = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  ? null
  : window.setInterval(() => {
      if (lightIndex < lights.length) {
        lights[lightIndex].classList.add('on');
        status.textContent = `SEÑAL ${lightIndex + 1} / 5`;
        lightIndex += 1;
        return;
      }
      window.clearInterval(lightTimer);
      lights.forEach((light) => light.classList.replace('on', 'out'));
      status.textContent = 'LUCES FUERA · ENTRÁ';
      window.setTimeout(openArchive, 440);
    }, 360);

skip.addEventListener('click', () => {
  if (lightTimer) window.clearInterval(lightTimer);
  openArchive();
});

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((element) => revealObserver.observe(element));

const destination = 'https://reward-hacking-sociales.vercel.app/';
const qrUrl = './qr-reward-hacking-sociales.png';
const qrImage = document.querySelector('#qr-image');
const openQr = document.querySelector('#open-qr');
qrImage.src = qrUrl;
openQr.href = qrUrl;

const copyButton = document.querySelector('#copy-url');
const copyStatus = document.querySelector('#copy-status');
copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(destination);
    copyStatus.textContent = 'URL COPIADA';
  } catch {
    copyStatus.textContent = destination;
  }
  window.setTimeout(() => { copyStatus.textContent = ''; }, 3200);
});

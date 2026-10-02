window.WallpaperCertificate = (function() {
    function renderCertificate(canvas, data) {
        const { studentName, score, domainScores, date } = data || {};
        canvas.width = 2400;
        canvas.height = 1696;
        const ctx = canvas.getContext('2d');
        const w = canvas.width;
        const h = canvas.height;

        // 1. Deep Space Stardust Nebula Background
        const bgGrad = ctx.createLinearGradient(0, 0, w, h);
        bgGrad.addColorStop(0, '#030a16');
        bgGrad.addColorStop(0.5, '#081d32');
        bgGrad.addColorStop(1, '#041518');
        ctx.fillStyle = bgGrad;
        ctx.fillRect(0, 0, w, h);

        // Subtle molecular carbon hexagonal rings
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.03)';
        ctx.lineWidth = 2;
        for (let i = 0; i < 20; i++) {
            drawHexagon(ctx, Math.random() * w, Math.random() * h, 50 + Math.random() * 150);
        }

        // Bohr atom electron orbital ellipses
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.02)';
        for (let i = 0; i < 10; i++) {
            ctx.beginPath();
            ctx.ellipse(Math.random() * w, Math.random() * h, 200 + Math.random() * 300, 50 + Math.random() * 100, Math.random() * Math.PI, 0, Math.PI * 2);
            ctx.stroke();
        }

        // 280 twinkling stardust particles
        for (let i = 0; i < 280; i++) {
            ctx.fillStyle = `rgba(255, 255, 255, ${Math.random() * 0.8 + 0.2})`;
            ctx.beginPath();
            ctx.arc(Math.random() * w, Math.random() * h, Math.random() * 2.5 + 0.5, 0, Math.PI * 2);
            ctx.fill();
        }

        // 2. Holographic Double Guilloché Gold Border
        const margin = 120;
        drawGuillocheBorder(ctx, margin, margin, w - margin * 2, h - margin * 2);

        // Beaded perimeter pearls
        drawPearls(ctx, margin - 20, margin - 20, w - (margin - 20) * 2, h - (margin - 20) * 2);

        // 4 corner celestial rosettes
        drawRosette(ctx, margin, margin, 60);
        drawRosette(ctx, w - margin, margin, 60);
        drawRosette(ctx, margin, h - margin, 60);
        drawRosette(ctx, w - margin, h - margin, 60);

        // 3. Official Credential Text
        ctx.textAlign = 'center';
        
        // Title
        ctx.fillStyle = '#FFD700';
        ctx.font = 'bold 50px "Times New Roman", serif';
        ctx.fillText('ROYAL THAI MEP SCIENCE ACADEMY & RESEARCH GUILD', w / 2, margin + 150);

        ctx.fillStyle = '#FFFFFF';
        ctx.font = 'bold 80px "Georgia", serif';
        ctx.fillText('OFFICIAL JUNIOR SCIENTIST DIPLOMA', w / 2, margin + 280);

        ctx.fillStyle = '#A0C0FF';
        ctx.font = 'italic 40px "Georgia", serif';
        ctx.fillText('Thai Rath Witthaya 75 · Mini English Program', w / 2, margin + 350);
        
        // This certifies that
        ctx.fillStyle = '#DDDDDD';
        ctx.font = '40px "Georgia", serif';
        ctx.fillText('This certifies that', w / 2, margin + 480);

        // 4. 3D Extruded Luminous Gold Student Name
        draw3DText(ctx, studentName || "Junior Explorer", w / 2, margin + 650);

        // Final marks and rank
        ctx.fillStyle = '#DDDDDD';
        ctx.font = '40px "Georgia", serif';
        ctx.fillText(`Has successfully completed the Science Quest with a score of ${score !== undefined ? score : 15} / 15`, w / 2, margin + 780);
        
        ctx.fillStyle = '#FFD700';
        ctx.font = 'bold 60px "Georgia", serif';
        ctx.fillText(`Rank: ${getRank(score !== undefined ? score : 15)}`, w / 2, margin + 880);

        // 5. 15-Star Dynamic Constellation Matrix
        const capsules = [
            { label: "Magnetic Forces", key: "forces" },
            { label: "Motion & Friction", key: "friction" }, // Fallback logic for keys in constellation
            { label: "Thermal Changes", key: "thermal" },
            { label: "Animal Needs", key: "needs" },
            { label: "Life Cycles", key: "cycles" }
        ];
        drawConstellationMatrix(ctx, w / 2, margin + 1050, capsules, domainScores);

        // 6. Official 32-Point Gold Embossed Academy Seal (Lower Right)
        drawSeal(ctx, w - margin - 250, h - margin - 250, 150);

        // 7. Procedural Security QR Code & Examiner Signature (Lower Left)
        drawQRCode(ctx, margin + 200, h - margin - 300, 150);
        
        ctx.fillStyle = '#DDDDDD';
        ctx.font = '24px monospace';
        ctx.textAlign = 'left';
        const hashStr = (studentName || '') + (score || '') + (date || '');
        ctx.fillText(`HASH: ${generateHash(hashStr)}`, margin + 120, h - margin - 100);
        ctx.fillText(`DATE: ${date || new Date().toISOString().split('T')[0]}`, margin + 120, h - margin - 60);

        // Signature
        ctx.strokeStyle = '#FFFFFF';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(margin + 500, h - margin - 180);
        ctx.quadraticCurveTo(margin + 550, h - margin - 220, margin + 600, h - margin - 150);
        ctx.quadraticCurveTo(margin + 650, h - margin - 100, margin + 700, h - margin - 200);
        ctx.quadraticCurveTo(margin + 750, h - margin - 250, margin + 800, h - margin - 180);
        ctx.stroke();

        ctx.fillStyle = '#DDDDDD';
        ctx.font = 'italic 30px "Times New Roman", serif';
        ctx.fillText('Prof. Oliver Newton, Ph.D.', margin + 520, h - margin - 120);
        ctx.font = '24px "Times New Roman", serif';
        ctx.fillText('Chief Examiner', margin + 580, h - margin - 80);
    }

    function getRank(score) {
        if (score === 15) return "Grand Master Junior Scientist";
        if (score >= 12) return "Master Junior Scientist";
        if (score >= 8) return "Advanced Junior Scientist";
        return "Junior Scientist";
    }

    function drawHexagon(ctx, x, y, size) {
        ctx.beginPath();
        for (let i = 0; i < 6; i++) {
            const angle = i * Math.PI / 3;
            const px = x + size * Math.cos(angle);
            const py = y + size * Math.sin(angle);
            if (i === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
        }
        ctx.closePath();
        ctx.stroke();
    }

    function drawGuillocheBorder(ctx, x, y, w, h) {
        ctx.strokeStyle = '#FFD700';
        ctx.lineWidth = 1;
        
        ctx.strokeRect(x, y, w, h);
        ctx.strokeRect(x + 15, y + 15, w - 30, h - 30);
        ctx.strokeRect(x + 30, y + 30, w - 60, h - 60);

        ctx.beginPath();
        for(let i = x; i <= x + w; i += 15) {
            ctx.arc(i, y + 15, 15, 0, Math.PI);
            ctx.arc(i, y + h - 15, 15, Math.PI, Math.PI * 2);
        }
        for(let j = y; j <= y + h; j += 15) {
            ctx.arc(x + 15, j, 15, Math.PI * 0.5, Math.PI * 1.5);
            ctx.arc(x + w - 15, j, 15, Math.PI * 1.5, Math.PI * 2.5);
        }
        ctx.stroke();
    }

    function drawPearls(ctx, x, y, w, h) {
        ctx.fillStyle = '#FFFFFF';
        const spacing = 40;
        const radius = 6;
        for (let i = x; i <= x + w; i += spacing) {
            drawPearl(ctx, i, y, radius);
            drawPearl(ctx, i, y + h, radius);
        }
        for (let j = y; j <= y + h; j += spacing) {
            drawPearl(ctx, x, j, radius);
            drawPearl(ctx, x + w, j, radius);
        }
    }

    function drawPearl(ctx, x, y, r) {
        const grad = ctx.createRadialGradient(x - r*0.3, y - r*0.3, r*0.1, x, y, r);
        grad.addColorStop(0, '#FFFFFF');
        grad.addColorStop(0.5, '#E0E0E0');
        grad.addColorStop(1, '#888888');
        ctx.beginPath();
        ctx.arc(x, y, r, 0, Math.PI * 2);
        ctx.fillStyle = grad;
        ctx.fill();
        ctx.strokeStyle = '#555555';
        ctx.lineWidth = 1;
        ctx.stroke();
    }

    function drawRosette(ctx, x, y, r) {
        ctx.fillStyle = '#081d32';
        ctx.beginPath();
        ctx.arc(x, y, r, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#FFD700';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.beginPath();
        for (let i = 0; i < 12; i++) {
            const angle = i * Math.PI / 6;
            ctx.ellipse(x, y, r * 0.8, r * 0.2, angle, 0, Math.PI * 2);
        }
        ctx.stroke();

        ctx.fillStyle = '#FFD700';
        ctx.beginPath();
        ctx.arc(x, y, r * 0.3, 0, Math.PI * 2);
        ctx.fill();
    }

    function draw3DText(ctx, text, x, y) {
        ctx.font = 'bold 120px "Georgia", serif';
        ctx.textAlign = 'center';
        
        const depth = 8;
        for (let i = depth; i > 0; i--) {
            ctx.fillStyle = `rgb(${150 - i*10}, ${100 - i*8}, 0)`;
            ctx.fillText(text, x + i, y + i);
        }
        
        const grad = ctx.createLinearGradient(x, y - 100, x, y);
        grad.addColorStop(0, '#FFFBE0');
        grad.addColorStop(0.5, '#FFD700');
        grad.addColorStop(1, '#B8860B');
        ctx.fillStyle = grad;
        ctx.fillText(text, x, y);

        ctx.lineWidth = 2;
        ctx.strokeStyle = '#FFFFFF';
        ctx.strokeText(text, x, y);

        const textWidth = ctx.measureText(text).width;
        drawSparkle(ctx, x - textWidth/2 - 20, y - 80);
        drawSparkle(ctx, x + textWidth/2 + 20, y - 20);
    }

    function drawSparkle(ctx, x, y) {
        ctx.fillStyle = '#FFFFFF';
        ctx.beginPath();
        ctx.moveTo(x, y - 15);
        ctx.quadraticCurveTo(x, y, x + 15, y);
        ctx.quadraticCurveTo(x, y, x, y + 15);
        ctx.quadraticCurveTo(x, y, x - 15, y);
        ctx.quadraticCurveTo(x, y, x, y - 15);
        ctx.fill();
    }

    function drawConstellationMatrix(ctx, cx, cy, capsules, domainScores = {}) {
        const totalWidth = 1800;
        const spacing = totalWidth / 5;
        const startX = cx - totalWidth / 2 + spacing / 2;

        capsules.forEach((cap, i) => {
            const x = startX + i * spacing;
            const y = cy;

            ctx.fillStyle = 'rgba(4, 21, 24, 0.8)';
            ctx.strokeStyle = '#FFD700';
            ctx.lineWidth = 3;
            ctx.beginPath();
            
            const rx = x - 140, ry = y - 50, rw = 280, rh = 160, r = 20;
            ctx.moveTo(rx + r, ry);
            ctx.lineTo(rx + rw - r, ry);
            ctx.quadraticCurveTo(rx + rw, ry, rx + rw, ry + r);
            ctx.lineTo(rx + rw, ry + rh - r);
            ctx.quadraticCurveTo(rx + rw, ry + rh, rx + rw - r, ry + rh);
            ctx.lineTo(rx + r, ry + rh);
            ctx.quadraticCurveTo(rx, ry + rh, rx, ry + rh - r);
            ctx.lineTo(rx, ry + r);
            ctx.quadraticCurveTo(rx, ry, rx + r, ry);
            ctx.fill();
            ctx.stroke();

            ctx.fillStyle = '#A0C0FF';
            ctx.font = 'bold 24px "Arial", sans-serif';
            ctx.fillText(cap.label, x, y - 10);

            // Default to 3 stars if score not found or provided for visuals
            let correct = 3;
            if (domainScores && domainScores[cap.key]) {
                correct = domainScores[cap.key].correct;
            } else if (domainScores && domainScores['forces'] && cap.key === 'friction') {
                // Handle naming edge cases if state just has 'forces'
                correct = domainScores['forces'].correct;
            }

            for (let j = 0; j < 3; j++) {
                const sx = x - 60 + j * 60;
                const sy = y + 50;
                const earned = j < correct;
                drawStar(ctx, sx, sy, 5, 20, 10, earned);
            }
        });
    }

    function drawStar(ctx, cx, cy, spikes, outerRadius, innerRadius, earned) {
        let rot = Math.PI / 2 * 3;
        let x = cx;
        let y = cy;
        let step = Math.PI / spikes;

        ctx.beginPath();
        ctx.moveTo(cx, cy - outerRadius);
        for (let i = 0; i < spikes; i++) {
            x = cx + Math.cos(rot) * outerRadius;
            y = cy + Math.sin(rot) * outerRadius;
            ctx.lineTo(x, y);
            rot += step;

            x = cx + Math.cos(rot) * innerRadius;
            y = cy + Math.sin(rot) * innerRadius;
            ctx.lineTo(x, y);
            rot += step;
        }
        ctx.lineTo(cx, cy - outerRadius);
        ctx.closePath();
        
        if (earned) {
            const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, outerRadius);
            grad.addColorStop(0, '#FFFFFF');
            grad.addColorStop(0.3, '#FFD700');
            grad.addColorStop(1, '#B8860B');
            ctx.fillStyle = grad;
            ctx.fill();
            ctx.strokeStyle = '#FFFFFF';
            ctx.lineWidth = 1;
            ctx.stroke();
        } else {
            ctx.fillStyle = 'rgba(255, 215, 0, 0.1)';
            ctx.fill();
            ctx.strokeStyle = 'rgba(255, 215, 0, 0.5)';
            ctx.lineWidth = 2;
            ctx.stroke();
        }
    }

    function drawSeal(ctx, x, y, r) {
        ctx.fillStyle = '#B8860B';
        ctx.beginPath();
        ctx.moveTo(x - 40, y + r - 20);
        ctx.lineTo(x - 80, y + r + 120);
        ctx.lineTo(x - 30, y + r + 90);
        ctx.lineTo(x + 20, y + r + 120);
        ctx.lineTo(x + 40, y + r - 20);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#FFD700';
        ctx.beginPath();
        const spikes = 32;
        const outer = r;
        const inner = r * 0.9;
        for (let i = 0; i < spikes * 2; i++) {
            const radius = i % 2 === 0 ? outer : inner;
            const angle = i * Math.PI / spikes;
            ctx.lineTo(x + Math.cos(angle) * radius, y + Math.sin(angle) * radius);
        }
        ctx.closePath();
        
        const grad = ctx.createRadialGradient(x - r*0.2, y - r*0.2, r*0.1, x, y, r);
        grad.addColorStop(0, '#FFFBE0');
        grad.addColorStop(0.5, '#FFD700');
        grad.addColorStop(1, '#8B6508');
        ctx.fillStyle = grad;
        ctx.fill();
        ctx.strokeStyle = '#553300';
        ctx.lineWidth = 4;
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(x, y, r * 0.8, 0, Math.PI * 2);
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(x, y, r * 0.75, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = '#553300';
        ctx.font = 'bold 16px "Georgia", serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        
        const text = 'MEP SCIENCE EXCELLENCE · PRIMARY 3 · ';
        drawTextAlongArc(ctx, text, x, y, r * 0.62, 0);
        
        ctx.fillStyle = '#553300';
        ctx.font = 'bold 45px "Georgia", serif';
        ctx.fillText('🔬', x - 20, y - 10);
        ctx.fillText('⚛️', x + 20, y + 15);
    }

    function drawTextAlongArc(ctx, str, cx, cy, radius, angle) {
        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(angle);
        for (let i = 0; i < str.length; i++) {
            ctx.save();
            ctx.rotate(i * (Math.PI * 2 / str.length) - Math.PI / 2);
            ctx.translate(0, -radius);
            ctx.fillText(str[i], 0, 0);
            ctx.restore();
        }
        ctx.restore();
    }

    function drawQRCode(ctx, x, y, size) {
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(x, y, size, size);
        
        ctx.fillStyle = '#000000';
        const cells = 21;
        const cellSize = size / cells;
        
        for(let r=0; r<cells; r++) {
            for(let c=0; c<cells; c++) {
                if ((r<7 && c<7) || (r<7 && c>=cells-7) || (r>=cells-7 && c<7)) {
                    if (r===0||r===6||c===0||c===6 || (r>1&&r<5&&c>1&&c<5)) {
                        ctx.fillRect(x + c*cellSize, y + r*cellSize, cellSize, cellSize);
                    }
                    continue;
                }
                if (Math.random() > 0.5) {
                    ctx.fillRect(x + c*cellSize, y + r*cellSize, cellSize, cellSize);
                }
            }
        }
    }

    function generateHash(input) {
        let hash = 0;
        if (!input) return "00000000";
        for (let i = 0; i < input.length; i++) {
            const char = input.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash;
        }
        return Math.abs(hash).toString(16).toUpperCase().padStart(8, '0');
    }

    function downloadWallpaper(canvas, filename = 'Science_Certificate.png') {
        const link = document.createElement('a');
        link.download = filename;
        link.href = canvas.toDataURL('image/png');
        link.click();
    }

    function printCertificate(canvas) {
        const imgData = canvas.toDataURL('image/png');
        const printWindow = window.open('', '_blank');
        if (!printWindow) return;
        printWindow.document.write(`
            <html>
                <head>
                    <title>Print Certificate</title>
                    <style>
                        @media print {
                            @page { size: A4 landscape; margin: 0; }
                            body { margin: 0; padding: 0; }
                            img { width: 100%; height: 100%; object-fit: cover; }
                        }
                        body { margin: 0; text-align: center; background: #333; }
                        img { max-width: 100%; height: auto; display: block; }
                    </style>
                </head>
                <body>
                    <img src="${imgData}" onload="window.print(); window.close();" />
                </body>
            </html>
        `);
        printWindow.document.close();
    }

    return {
        renderCertificate,
        downloadWallpaper,
        printCertificate
    };
})();

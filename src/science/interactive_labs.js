window.InteractiveLabs = (function() {
  
  function triggerCompletion(labId) {
    if (window.ScienceApp && window.ScienceApp.onLabCompleted) {
      window.ScienceApp.onLabCompleted(labId);
    }
  }
  
  function createResetButton(container, mountFn) {
    const btn = document.createElement('button');
    btn.innerText = 'Reset Lab';
    btn.style.cssText = 'position: absolute; top: 10px; right: 10px; padding: 8px 16px; background: #ff4757; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; z-index: 100;';
    btn.onclick = () => mountFn(container);
    return btn;
  }

  function mountMagnetLab(container) {
    container.innerHTML = '';
    container.style.position = 'relative';
    container.style.width = '100%';
    container.style.height = '100%';
    container.style.minHeight = '400px';
    container.style.background = '#f1f2f6';
    container.style.overflow = 'hidden';
    container.appendChild(createResetButton(container, mountMagnetLab));

    const html = `
      <div style="padding: 20px; font-family: sans-serif;">
        <h2 style="margin-top:0;">Magnetic Physics & Sorting Workshop</h2>
        <div style="display: flex; gap: 20px;">
          <!-- Bar Magnets Track -->
          <div style="flex: 1; border: 2px dashed #ccc; padding: 20px; position: relative; height: 150px; background: white; border-radius: 10px;">
            <h4>Dual Bar Magnets Track</h4>
            <div id="magnet1" style="width: 100px; height: 40px; background: linear-gradient(to right, red 50%, blue 50%); position: absolute; top: 80px; left: 50px; cursor: grab; display: flex; color: white; font-weight: bold; align-items: center; justify-content: space-between; padding: 0 10px; box-sizing: border-box; user-select: none;">
              <span>N</span><span>S</span>
            </div>
            <div id="magnet2" style="width: 100px; height: 40px; background: linear-gradient(to right, red 50%, blue 50%); position: absolute; top: 80px; left: 300px; cursor: grab; display: flex; color: white; font-weight: bold; align-items: center; justify-content: space-between; padding: 0 10px; box-sizing: border-box; user-select: none;">
              <span>N</span><span>S</span>
            </div>
            <div id="magnetic-field" style="position: absolute; top:0; left:0; width:100%; height:100%; pointer-events: none;"></div>
          </div>
        </div>
        
        <div style="margin-top: 20px; display: flex; gap: 20px;">
          <!-- Magnetic Specimen Tray -->
          <div style="flex: 2; border: 2px solid #ccc; padding: 20px; background: white; border-radius: 10px; position: relative; height: 200px;">
            <h4>Magnetic Test Tray (Drag Horseshoe over items)</h4>
            <div id="horseshoe" style="width: 60px; height: 60px; background: url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><path d=%22M 20,80 L 20,40 A 30,30 0 0,1 80,40 L 80,80 L 60,80 L 60,40 A 10,10 0 0,0 40,40 L 40,80 Z%22 fill=%22red%22 stroke=%22silver%22 stroke-width=%224%22/><rect x=%2220%22 y=%2280%22 width=%2220%22 height=%2210%22 fill=%22silver%22/><rect x=%2260%22 y=%2280%22 width=%2220%22 height=%2210%22 fill=%22silver%22/></svg>') no-repeat center; background-size: contain; position: absolute; top: 20px; right: 20px; cursor: grab; z-index: 10;"></div>
            
            <div id="items-tray" style="display: flex; gap: 15px; margin-top: 50px; flex-wrap: wrap;">
              <div class="test-item" data-magnetic="true" style="width: 40px; height: 40px; background: gray; border-radius: 5px; text-align: center; line-height: 40px; font-size: 10px; user-select:none;">Nail</div>
              <div class="test-item" data-magnetic="true" style="width: 40px; height: 40px; background: silver; border-radius: 5px; text-align: center; line-height: 40px; font-size: 10px; user-select:none;">Clip</div>
              <div class="test-item" data-magnetic="true" style="width: 40px; height: 40px; background: #aaa; border-radius: 50%; text-align: center; line-height: 40px; font-size: 10px; user-select:none;">Washer</div>
              <div class="test-item" data-magnetic="true" style="width: 40px; height: 40px; background: gold; border-radius: 5px; text-align: center; line-height: 40px; font-size: 10px; user-select:none;">Key</div>
              <div class="test-item" data-magnetic="false" style="width: 40px; height: 40px; background: #eccc68; border-radius: 5px; text-align: center; line-height: 40px; font-size: 10px; user-select:none;">Pencil</div>
              <div class="test-item" data-magnetic="false" style="width: 40px; height: 40px; background: rgba(255,255,255,0.8); border: 1px solid #ccc; text-align: center; line-height: 40px; font-size: 10px; user-select:none;">Ruler</div>
              <div class="test-item" data-magnetic="false" style="width: 40px; height: 40px; background: pink; border-radius: 5px; text-align: center; line-height: 40px; font-size: 10px; user-select:none;">Eraser</div>
              <div class="test-item" data-magnetic="false" style="width: 40px; height: 40px; background: lightblue; border-radius: 50%; text-align: center; line-height: 40px; font-size: 10px; user-select:none;">Marble</div>
            </div>
          </div>
          <!-- Bins -->
          <div style="flex: 1; border: 2px dashed #2ed573; padding: 20px; background: #e8f8f5; border-radius: 10px; text-align: center;" id="ferrous-bin">
            <h4>Ferrous Bin</h4>
            <div id="ferrous-count" style="font-size: 24px; font-weight: bold; color: #2ed573;">0 / 4</div>
          </div>
        </div>
      </div>
    `;
    container.insertAdjacentHTML('beforeend', html);

    let ferrousCount = 0;
    let trackTested = false;

    // Track logic (simplified drag & attract/repel)
    const m1 = container.querySelector('#magnet1');
    const m2 = container.querySelector('#magnet2');
    
    function makeDraggable(el, onDrag) {
      let isDragging = false;
      let startX, startY, initialX, initialY;
      el.addEventListener('mousedown', e => {
        isDragging = true;
        startX = e.clientX; startY = e.clientY;
        initialX = el.offsetLeft; initialY = el.offsetTop;
        el.style.zIndex = 100;
      });
      document.addEventListener('mousemove', e => {
        if (!isDragging) return;
        const dx = e.clientX - startX;
        const dy = e.clientY - startY;
        el.style.left = initialX + dx + 'px';
        el.style.top = initialY + dy + 'px';
        if (onDrag) onDrag();
      });
      document.addEventListener('mouseup', () => {
        if (isDragging) {
          isDragging = false;
          el.style.zIndex = '';
          if (onDrag) onDrag();
        }
      });
    }

    makeDraggable(m1, checkMagnets);
    makeDraggable(m2, checkMagnets);

    function checkMagnets() {
      const rect1 = m1.getBoundingClientRect();
      const rect2 = m2.getBoundingClientRect();
      const dist = Math.abs(rect1.left - rect2.left);
      if (dist < 120 && dist > 0) {
        trackTested = true;
        if (rect1.left < rect2.left) {
          // m1 is left of m2
          // S of m1 attracts N of m2
          m1.style.left = (m2.offsetLeft - 100) + 'px';
        } else {
          // m2 is left of m1
          m2.style.left = (m1.offsetLeft - 100) + 'px';
        }
        checkWin();
      }
    }

    // Horseshoe logic
    const horseshoe = container.querySelector('#horseshoe');
    const items = container.querySelectorAll('.test-item');
    const bin = container.querySelector('#ferrous-bin');

    makeDraggable(horseshoe, () => {
      const hRect = horseshoe.getBoundingClientRect();
      items.forEach(item => {
        if (item.style.display === 'none') return;
        const iRect = item.getBoundingClientRect();
        const dist = Math.hypot(hRect.left - iRect.left, hRect.top - iRect.top);
        
        if (dist < 50) {
          if (item.dataset.magnetic === 'true') {
            item.style.display = 'none';
            ferrousCount++;
            container.querySelector('#ferrous-count').innerText = ferrousCount + ' / 4';
            checkWin();
          } else {
            item.style.transform = 'translateY(10px)';
            setTimeout(() => item.style.transform = 'translateY(0)', 200);
          }
        }
      });
    });

    function checkWin() {
      if (trackTested && ferrousCount >= 4) {
        setTimeout(() => triggerCompletion('magnet'), 500);
      }
    }
  }

  function mountFrictionLab(container) {
    container.innerHTML = '';
    container.style.position = 'relative';
    container.style.width = '100%';
    container.style.height = '100%';
    container.style.minHeight = '400px';
    container.style.background = '#f1f2f6';
    container.style.overflow = 'hidden';
    container.appendChild(createResetButton(container, mountFrictionLab));

    const html = `
      <div style="padding: 20px; font-family: sans-serif;">
        <h2 style="margin-top:0;">Pip's Ramp & Friction Runway</h2>
        
        <div style="margin-bottom: 10px;">
          <label><strong>Incline:</strong></label>
          <select id="incline-select">
            <option value="15">15° Low</option>
            <option value="30">30° Medium</option>
            <option value="45">45° Steep</option>
          </select>
          
          <label style="margin-left: 20px;"><strong>Surface:</strong></label>
          <select id="surface-select">
            <option value="ice">Ice Sheet</option>
            <option value="tile">Polished Tile</option>
            <option value="wood">Smooth Wood</option>
            <option value="carpet">Felt Carpet</option>
            <option value="sandpaper">Rough Sandpaper</option>
          </select>
          
          <button id="launch-btn" style="margin-left: 20px; padding: 5px 15px; background: #1e90ff; color: white; border: none; border-radius: 5px; cursor: pointer;">Launch Car</button>
        </div>

        <div style="position: relative; height: 300px; background: white; border-radius: 10px; border: 1px solid #ccc; overflow: hidden; margin-top: 20px;">
          <!-- Speedometer -->
          <div id="speedometer" style="position: absolute; top: 10px; right: 20px; font-size: 24px; font-weight: bold; color: #ff4757;">0 km/h</div>
          
          <!-- Ramp -->
          <div id="ramp" style="position: absolute; left: 0; bottom: 50px; width: 150px; height: 5px; background: #57606f; transform-origin: left bottom; transform: rotate(15deg);"></div>
          
          <!-- Runway -->
          <div id="runway" style="position: absolute; left: 145px; bottom: 50px; width: calc(100% - 145px); height: 5px; background: #7bed9f;"></div>
          
          <!-- Car -->
          <div id="car" style="position: absolute; left: 130px; bottom: 55px; width: 40px; height: 20px; background: #ff4757; border-radius: 10px 10px 0 0; z-index: 10; transition: left 2s cubic-bezier(0.25, 1, 0.5, 1);"></div>
          
          <!-- Ghost Car -->
          <div id="ghost-car" style="position: absolute; left: 130px; bottom: 55px; width: 40px; height: 20px; background: rgba(255, 71, 87, 0.3); border-radius: 10px 10px 0 0; z-index: 5; display: none;"></div>
          
          <!-- Flag -->
          <div id="flag" style="position: absolute; bottom: 55px; left: 130px; font-size: 24px; display: none; transition: left 0.5s;">🚩</div>
        </div>
      </div>
    `;
    container.insertAdjacentHTML('beforeend', html);

    const inclineSelect = container.querySelector('#incline-select');
    const surfaceSelect = container.querySelector('#surface-select');
    const launchBtn = container.querySelector('#launch-btn');
    const ramp = container.querySelector('#ramp');
    const runway = container.querySelector('#runway');
    const car = container.querySelector('#car');
    const ghostCar = container.querySelector('#ghost-car');
    const flag = container.querySelector('#flag');
    const speedometer = container.querySelector('#speedometer');
    
    let testedSurfaces = new Set();
    let lastDist = 0;
    let isRunning = false;

    const surfaceFriction = {
      ice: 0.1,
      tile: 0.3,
      wood: 0.5,
      carpet: 0.7,
      sandpaper: 0.9
    };

    const surfaceColors = {
      ice: '#c7ecee',
      tile: '#f5f6fa',
      wood: '#d1ccc0',
      carpet: '#eb4d4b',
      sandpaper: '#535c68'
    };

    inclineSelect.addEventListener('change', (e) => {
      ramp.style.transform = `rotate(${e.target.value}deg)`;
      resetPositions();
    });

    surfaceSelect.addEventListener('change', (e) => {
      runway.style.background = surfaceColors[e.target.value];
      resetPositions();
    });
    
    function resetPositions() {
      if(isRunning) return;
      car.style.transition = 'none';
      car.style.left = '130px';
      car.style.bottom = '55px'; // Adjust based on ramp later if needed
      speedometer.innerText = '0 km/h';
      flag.style.display = 'none';
    }

    launchBtn.addEventListener('click', () => {
      if (isRunning) return;
      isRunning = true;
      
      const surface = surfaceSelect.value;
      const angle = parseInt(inclineSelect.value);
      
      testedSurfaces.add(surface);
      
      if (lastDist > 0) {
        ghostCar.style.display = 'block';
        ghostCar.style.left = lastDist + 'px';
      }

      // Calculate distance based on angle and friction
      const baseDist = angle * 10; 
      const friction = surfaceFriction[surface];
      const dist = 130 + (baseDist / friction) * 0.5; // arbitrary formula for visual
      
      car.style.transition = 'left 2s cubic-bezier(0.25, 1, 0.5, 1)';
      car.style.left = Math.min(dist, container.offsetWidth - 50) + 'px';
      
      let speed = angle * 2;
      let interval = setInterval(() => {
        if(speed > 0) speed -= (friction * 5);
        if(speed < 0) speed = 0;
        speedometer.innerText = Math.round(speed) + ' km/h';
      }, 100);

      setTimeout(() => {
        clearInterval(interval);
        speedometer.innerText = '0 km/h';
        lastDist = parseFloat(car.style.left);
        flag.style.display = 'block';
        flag.style.left = (lastDist + 10) + 'px';
        isRunning = false;
        
        if (testedSurfaces.size >= 2) {
          triggerCompletion('friction');
        }
      }, 2000);
    });
    
    // Init styles
    runway.style.background = surfaceColors[surfaceSelect.value];
  }

  function mountThermalLab(container) {
    container.innerHTML = '';
    container.style.position = 'relative';
    container.style.width = '100%';
    container.style.height = '100%';
    container.style.minHeight = '400px';
    container.style.background = '#f1f2f6';
    container.style.overflow = 'hidden';
    container.appendChild(createResetButton(container, mountThermalLab));

    const html = `
      <div style="padding: 20px; font-family: sans-serif;">
        <h2 style="margin-top:0;">Thermal Transformation Station</h2>
        
        <div style="display: flex; gap: 40px; margin-top: 30px;">
          <!-- Thermometer & Controls -->
          <div style="flex: 1; text-align: center; max-width: 200px;">
            <div style="height: 200px; width: 40px; border: 2px solid #ccc; border-radius: 20px; margin: 0 auto; position: relative; background: white; overflow: hidden;">
              <div id="thermo-liquid" style="position: absolute; bottom: 0; left: 0; width: 100%; height: 50%; background: red; transition: height 0.5s, background 0.5s;"></div>
            </div>
            <div style="margin-top: 20px;">
              <input type="range" id="temp-slider" min="-10" max="110" value="20" style="width: 100%;">
              <div id="temp-display" style="font-size: 24px; font-weight: bold; margin-top: 10px;">20°C</div>
            </div>
          </div>
          
          <!-- Test Pad -->
          <div style="flex: 2;">
            <div style="display: flex; gap: 10px; margin-bottom: 20px;">
              <button class="substance-btn" data-type="ice" style="padding: 10px; cursor: pointer;">Ice Cube</button>
              <button class="substance-btn" data-type="chocolate" style="padding: 10px; cursor: pointer;">Chocolate</button>
              <button class="substance-btn" data-type="wax" style="padding: 10px; cursor: pointer;">Wax</button>
              <button class="substance-btn" data-type="egg" style="padding: 10px; cursor: pointer;">Raw Egg</button>
            </div>
            
            <div id="test-pad" style="width: 200px; height: 200px; border: 4px solid #333; border-radius: 50%; display: flex; align-items: center; justify-content: center; position: relative; background: #fff; transition: background 0.5s, box-shadow 0.5s;">
              <div id="substance-view" style="font-size: 64px; transition: all 0.5s;"></div>
            </div>
          </div>
        </div>
      </div>
    `;
    container.insertAdjacentHTML('beforeend', html);

    const slider = container.querySelector('#temp-slider');
    const display = container.querySelector('#temp-display');
    const thermoLiquid = container.querySelector('#thermo-liquid');
    const testPad = container.querySelector('#test-pad');
    const substanceView = container.querySelector('#substance-view');
    const btns = container.querySelectorAll('.substance-btn');
    
    let currentTemp = 20;
    let currentSubstance = null;
    let eggCooked = false;
    let meltCount = 0;
    let cookedEgg = false;

    const substanceStates = {
      ice: { name: 'Ice', iconSolid: '🧊', iconLiquid: '💧', meltPoint: 0 },
      chocolate: { name: 'Chocolate', iconSolid: '🍫', iconLiquid: '🟤', meltPoint: 35 },
      wax: { name: 'Wax', iconSolid: '🕯️', iconLiquid: '🟡', meltPoint: 50 },
      egg: { name: 'Raw Egg', iconSolid: '🥚', iconLiquid: '🍳', meltPoint: 70 } // Treat liquid as cooked
    };

    function updateView() {
      // Thermometer
      const percent = ((currentTemp + 10) / 120) * 100;
      thermoLiquid.style.height = percent + '%';
      
      if(currentTemp > 60) {
        thermoLiquid.style.background = '#ff4757';
        testPad.style.background = '#ff6b81';
        testPad.style.boxShadow = '0 0 20px #ff4757';
      } else if (currentTemp < 10) {
        thermoLiquid.style.background = '#70a1ff';
        testPad.style.background = '#eccc68'; // mild
        testPad.style.boxShadow = '0 0 20px #70a1ff';
      } else {
        thermoLiquid.style.background = '#2ed573';
        testPad.style.background = '#fff';
        testPad.style.boxShadow = 'none';
      }

      display.innerText = currentTemp + '°C';

      // Substance
      if(currentSubstance) {
        const sub = substanceStates[currentSubstance];
        if(currentSubstance === 'egg') {
          if(currentTemp >= sub.meltPoint && !eggCooked) {
            eggCooked = true;
            cookedEgg = true;
            substanceView.innerHTML = sub.iconLiquid;
            alert("The heat permanently changed the protein! Irreversible change.");
            checkWin();
          }
          if(eggCooked) substanceView.innerHTML = sub.iconLiquid;
          else substanceView.innerHTML = sub.iconSolid;
        } else {
          if(currentTemp >= sub.meltPoint) {
            substanceView.innerHTML = sub.iconLiquid;
            substanceView.style.transform = 'scale(1.2) translateY(20px)';
            if(currentSubstance === 'chocolate' || currentSubstance === 'ice') {
                meltCount++;
                checkWin();
            }
          } else {
            substanceView.innerHTML = sub.iconSolid;
            substanceView.style.transform = 'scale(1) translateY(0)';
          }
        }
      }
    }

    slider.addEventListener('input', (e) => {
      currentTemp = parseInt(e.target.value);
      updateView();
    });

    btns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        currentSubstance = e.target.dataset.type;
        if(currentSubstance !== 'egg') eggCooked = false; // reset for non-egg
        updateView();
      });
    });
    
    function checkWin() {
        if(meltCount > 0 && cookedEgg) {
            setTimeout(() => triggerCompletion('thermal'), 1000);
        }
    }

    updateView();
  }

  function mountNutritionLab(container) {
    container.innerHTML = '';
    container.style.position = 'relative';
    container.style.width = '100%';
    container.style.height = '100%';
    container.style.minHeight = '400px';
    container.style.background = '#f1f2f6';
    container.style.overflow = 'hidden';
    container.appendChild(createResetButton(container, mountNutritionLab));

    const html = `
      <div style="padding: 20px; font-family: sans-serif;">
        <h2 style="margin-top:0;">Bio-Nutrition & Animal Feeder</h2>
        
        <div style="display: flex; gap: 20px;">
          <!-- Pods -->
          <div style="flex: 1; border: 2px solid #ccc; padding: 10px; border-radius: 10px; background: white;">
            <h4>Holographic Pods</h4>
            <div style="display: flex; justify-content: space-around; margin-top: 20px;">
              <div class="pod" data-type="carbs" style="width: 80px; height: 100px; border: 2px dashed #feca57; border-radius: 40px 40px 10px 10px; position: relative; text-align: center;">
                <div style="position: absolute; bottom: -25px; width: 100%; font-size: 12px; font-weight:bold;">Carbs (Energy)</div>
                <div class="pod-content" style="position: absolute; bottom:0; left:0; width:100%; height:0%; background: rgba(254, 202, 87, 0.5); border-radius: 0 0 10px 10px; transition: height 0.5s;"></div>
              </div>
              <div class="pod" data-type="protein" style="width: 80px; height: 100px; border: 2px dashed #ff6b6b; border-radius: 40px 40px 10px 10px; position: relative; text-align: center;">
                <div style="position: absolute; bottom: -25px; width: 100%; font-size: 12px; font-weight:bold;">Protein (Growth)</div>
                <div class="pod-content" style="position: absolute; bottom:0; left:0; width:100%; height:0%; background: rgba(255, 107, 107, 0.5); border-radius: 0 0 10px 10px; transition: height 0.5s;"></div>
              </div>
              <div class="pod" data-type="vitamins" style="width: 80px; height: 100px; border: 2px dashed #1dd1a1; border-radius: 40px 40px 10px 10px; position: relative; text-align: center;">
                <div style="position: absolute; bottom: -25px; width: 100%; font-size: 12px; font-weight:bold;">Vitamins</div>
                <div class="pod-content" style="position: absolute; bottom:0; left:0; width:100%; height:0%; background: rgba(29, 209, 161, 0.5); border-radius: 0 0 10px 10px; transition: height 0.5s;"></div>
              </div>
            </div>
            
            <div id="food-tray" style="display: flex; gap: 10px; justify-content: center; margin-top: 50px;">
              <div class="food-item" data-type="carbs" style="font-size: 32px; cursor: grab; user-select: none;">🍚</div>
              <div class="food-item" data-type="carbs" style="font-size: 32px; cursor: grab; user-select: none;">🍞</div>
              <div class="food-item" data-type="protein" style="font-size: 32px; cursor: grab; user-select: none;">🐟</div>
              <div class="food-item" data-type="protein" style="font-size: 32px; cursor: grab; user-select: none;">🍗</div>
              <div class="food-item" data-type="vitamins" style="font-size: 32px; cursor: grab; user-select: none;">🥦</div>
              <div class="food-item" data-type="vitamins" style="font-size: 32px; cursor: grab; user-select: none;">🥕</div>
            </div>
          </div>
          
          <!-- Diner -->
          <div style="flex: 1; border: 2px solid #ccc; padding: 10px; border-radius: 10px; background: white;">
            <h4>Animal Diner</h4>
            <div style="display: flex; flex-direction: column; gap: 15px;">
              <div class="animal" data-diet="herbivore" style="display: flex; align-items: center; gap: 10px; border: 1px solid #eee; padding: 10px; border-radius: 8px;">
                <div style="font-size: 40px;">🐰</div>
                <div>Herbivore (Plants)</div>
                <div class="plate" style="margin-left: auto; width: 50px; height: 50px; border: 2px dashed #ccc; border-radius: 50%; display: flex; align-items: center; justify-content: center;"></div>
              </div>
              <div class="animal" data-diet="carnivore" style="display: flex; align-items: center; gap: 10px; border: 1px solid #eee; padding: 10px; border-radius: 8px;">
                <div style="font-size: 40px;">🐯</div>
                <div>Carnivore (Meat)</div>
                <div class="plate" style="margin-left: auto; width: 50px; height: 50px; border: 2px dashed #ccc; border-radius: 50%; display: flex; align-items: center; justify-content: center;"></div>
              </div>
              <div class="animal" data-diet="omnivore" style="display: flex; align-items: center; gap: 10px; border: 1px solid #eee; padding: 10px; border-radius: 8px;">
                <div style="font-size: 40px;">🐻</div>
                <div>Omnivore (Both)</div>
                <div class="plate" style="margin-left: auto; width: 50px; height: 50px; border: 2px dashed #ccc; border-radius: 50%; display: flex; align-items: center; justify-content: center;"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
    container.insertAdjacentHTML('beforeend', html);

    const foods = container.querySelectorAll('.food-item');
    const pods = container.querySelectorAll('.pod');
    const plates = container.querySelectorAll('.plate');
    
    let podsFilled = 0;
    let animalsFed = 0;

    let podCounts = { carbs: 0, protein: 0, vitamins: 0 };

    foods.forEach(food => {
      let isDragging = false;
      let startX, startY, initialX, initialY;
      
      food.addEventListener('mousedown', e => {
        isDragging = true;
        startX = e.clientX; startY = e.clientY;
        const rect = food.getBoundingClientRect();
        food.style.position = 'absolute';
        food.style.zIndex = 1000;
        food.style.left = rect.left + 'px';
        food.style.top = rect.top + 'px';
        initialX = rect.left;
        initialY = rect.top;
      });

      document.addEventListener('mousemove', e => {
        if(!isDragging) return;
        food.style.left = initialX + (e.clientX - startX) + 'px';
        food.style.top = initialY + (e.clientY - startY) + 'px';
      });

      document.addEventListener('mouseup', e => {
        if(!isDragging) return;
        isDragging = false;
        food.style.zIndex = '';
        
        let dropped = false;

        // Check Pods
        pods.forEach(pod => {
          const pRect = pod.getBoundingClientRect();
          const fRect = food.getBoundingClientRect();
          if(fRect.left > pRect.left && fRect.right < pRect.right && fRect.top > pRect.top && fRect.bottom < pRect.bottom) {
            if(food.dataset.type === pod.dataset.type) {
              food.style.display = 'none';
              dropped = true;
              podCounts[food.dataset.type]++;
              const pct = Math.min(100, podCounts[food.dataset.type] * 50);
              pod.querySelector('.pod-content').style.height = pct + '%';
              if(pct === 100) podsFilled++;
              checkWin();
            }
          }
        });

        // Check Plates
        plates.forEach(plate => {
          const pRect = plate.getBoundingClientRect();
          const fRect = food.getBoundingClientRect();
          if(fRect.left > pRect.left - 20 && fRect.right < pRect.right + 20 && fRect.top > pRect.top - 20 && fRect.bottom < pRect.bottom + 20) {
            const diet = plate.parentElement.dataset.diet;
            const fType = food.dataset.type;
            const fIcon = food.innerText;
            
            let canEat = false;
            if(diet === 'herbivore' && fType === 'vitamins') canEat = true;
            if(diet === 'carnivore' && fType === 'protein') canEat = true;
            if(diet === 'omnivore') canEat = true; // simplifying
            
            if(canEat) {
              food.style.display = 'none';
              plate.innerText = fIcon;
              plate.style.borderColor = '#2ed573';
              dropped = true;
              animalsFed++;
              checkWin();
            } else {
              alert("This animal doesn't eat that!");
            }
          }
        });

        if(!dropped) {
          food.style.position = 'static';
        }
      });
    });

    function checkWin() {
      if(podsFilled >= 3 && animalsFed >= 3) {
        setTimeout(() => triggerCompletion('nutrition'), 500);
      }
    }
  }

  function mountLifecycleLab(container) {
    container.innerHTML = '';
    container.style.position = 'relative';
    container.style.width = '100%';
    container.style.height = '100%';
    container.style.minHeight = '500px';
    container.style.background = '#2f3640';
    container.style.color = 'white';
    container.style.overflow = 'hidden';
    container.appendChild(createResetButton(container, mountLifecycleLab));

    const html = `
      <div style="padding: 20px; font-family: sans-serif; text-align: center;">
        <h2 style="margin-top:0; color: #f5f6fa;">Life Cycle Astrolabe Wheel</h2>
        
        <div style="margin-bottom: 20px;">
          <button class="cycle-btn" data-cycle="butterfly" style="padding: 8px 16px; margin: 0 5px; cursor: pointer;">Butterfly</button>
          <button class="cycle-btn" data-cycle="frog" style="padding: 8px 16px; margin: 0 5px; cursor: pointer;">Frog</button>
          <button class="cycle-btn" data-cycle="chicken" style="padding: 8px 16px; margin: 0 5px; cursor: pointer;">Chicken</button>
        </div>
        
        <div style="position: relative; width: 400px; height: 400px; margin: 0 auto; border-radius: 50%; border: 4px solid #e1b12c; background: rgba(0,0,0,0.5);">
          <!-- Sockets -->
          <div class="socket" data-index="0" style="position: absolute; top: 10px; left: 160px; width: 80px; height: 80px; border: 2px dashed #e1b12c; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px;">1</div>
          <div class="socket" data-index="1" style="position: absolute; top: 160px; right: 10px; width: 80px; height: 80px; border: 2px dashed #e1b12c; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px;">2</div>
          <div class="socket" data-index="2" style="position: absolute; bottom: 10px; left: 160px; width: 80px; height: 80px; border: 2px dashed #e1b12c; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px;">3</div>
          <div class="socket" data-index="3" style="position: absolute; top: 160px; left: 10px; width: 80px; height: 80px; border: 2px dashed #e1b12c; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px;">4</div>
          
          <!-- Arrows -->
          <div style="position: absolute; top: 50px; right: 50px; font-size: 24px; transform: rotate(45deg);">➔</div>
          <div style="position: absolute; bottom: 50px; right: 50px; font-size: 24px; transform: rotate(135deg);">➔</div>
          <div style="position: absolute; bottom: 50px; left: 50px; font-size: 24px; transform: rotate(225deg);">➔</div>
          <div style="position: absolute; top: 50px; left: 50px; font-size: 24px; transform: rotate(315deg);">➔</div>
          
          <!-- Center Animation -->
          <div id="center-anim" style="position: absolute; top: 150px; left: 150px; width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; font-size: 64px; transition: transform 2s;"></div>
        </div>
        
        <div id="stages-tray" style="display: flex; gap: 15px; justify-content: center; margin-top: 20px; min-height: 80px;"></div>
      </div>
    `;
    container.insertAdjacentHTML('beforeend', html);

    const cycles = {
      butterfly: [ { id: 0, icon: '🥚', name: 'Egg' }, { id: 1, icon: '🐛', name: 'Caterpillar' }, { id: 2, icon: '🦋', name: 'Chrysalis' }, { id: 3, icon: '🦋', name: 'Adult' } ],
      frog: [ { id: 0, icon: '🥚', name: 'Egg' }, { id: 1, icon: '🐸', name: 'Tadpole' }, { id: 2, icon: '🐸', name: 'Froglet' }, { id: 3, icon: '🐸', name: 'Adult' } ],
      chicken: [ { id: 0, icon: '🥚', name: 'Egg' }, { id: 1, icon: '🐣', name: 'Hatching' }, { id: 2, icon: '🐥', name: 'Chick' }, { id: 3, icon: '🐔', name: 'Adult' } ]
    };

    const tray = container.querySelector('#stages-tray');
    const sockets = container.querySelectorAll('.socket');
    const btns = container.querySelectorAll('.cycle-btn');
    const centerAnim = container.querySelector('#center-anim');

    let currentSequence = [];
    let placedCount = 0;

    function loadCycle(cycleName) {
      tray.innerHTML = '';
      centerAnim.innerHTML = '';
      centerAnim.style.transform = 'rotate(0deg)';
      placedCount = 0;
      
      sockets.forEach(s => {
        s.innerHTML = s.dataset.index;
        s.style.borderColor = '#e1b12c';
      });

      const stages = [...cycles[cycleName]].sort(() => Math.random() - 0.5);
      
      stages.forEach(stage => {
        const el = document.createElement('div');
        el.className = 'stage-item';
        el.innerText = stage.icon;
        el.dataset.id = stage.id;
        el.style.cssText = 'width: 60px; height: 60px; background: white; color: black; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px; cursor: grab; user-select: none;';
        
        makeDraggableStage(el);
        tray.appendChild(el);
      });
    }

    function makeDraggableStage(el) {
      let isDragging = false;
      let startX, startY, initialX, initialY;
      
      el.addEventListener('mousedown', e => {
        isDragging = true;
        startX = e.clientX; startY = e.clientY;
        const rect = el.getBoundingClientRect();
        el.style.position = 'absolute';
        el.style.zIndex = 1000;
        el.style.left = rect.left + 'px';
        el.style.top = rect.top + 'px';
        initialX = rect.left;
        initialY = rect.top;
      });

      document.addEventListener('mousemove', e => {
        if(!isDragging) return;
        el.style.left = initialX + (e.clientX - startX) + 'px';
        el.style.top = initialY + (e.clientY - startY) + 'px';
      });

      document.addEventListener('mouseup', e => {
        if(!isDragging) return;
        isDragging = false;
        el.style.zIndex = '';
        
        let dropped = false;
        sockets.forEach(socket => {
          const sRect = socket.getBoundingClientRect();
          const eRect = el.getBoundingClientRect();
          
          if(eRect.left > sRect.left - 30 && eRect.right < sRect.right + 30 && eRect.top > sRect.top - 30 && eRect.bottom < sRect.bottom + 30) {
            if(socket.dataset.index === el.dataset.id) {
              socket.innerHTML = el.innerText;
              socket.style.borderColor = '#2ed573';
              el.style.display = 'none';
              dropped = true;
              placedCount++;
              checkWin();
            } else {
              el.style.position = 'static';
            }
          }
        });

        if(!dropped) {
          el.style.position = 'static';
        }
      });
    }

    function checkWin() {
      if(placedCount === 4) {
        centerAnim.innerHTML = '✨';
        centerAnim.style.transform = 'rotate(720deg) scale(1.5)';
        setTimeout(() => triggerCompletion('lifecycle'), 2000);
      }
    }

    btns.forEach(btn => {
      btn.addEventListener('click', e => {
        loadCycle(e.target.dataset.cycle);
      });
    });

    // Load default
    loadCycle('butterfly');
  }

  return {
    mountLab: function(containerId, labId) {
      const container = document.getElementById(containerId);
      if (!container) return;
      
      switch(labId) {
        case 'magnet': mountMagnetLab(container); break;
        case 'friction': mountFrictionLab(container); break;
        case 'thermal': mountThermalLab(container); break;
        case 'nutrition': mountNutritionLab(container); break;
        case 'lifecycle': mountLifecycleLab(container); break;
        default: container.innerHTML = 'Lab not found.';
      }
    },
    mountMagnetLab,
    mountFrictionLab,
    mountThermalLab,
    mountNutritionLab,
    mountLifecycleLab
  };
})();

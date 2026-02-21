import { Component } from '@angular/core';

@Component({
  selector: 'app-login-card',
  template: `
    <div class="card" style="background: #f8fafc; backdrop-filter: blur(10px); border-radius: 8px; padding: 24px; border: 1px solid #6366f1; box-shadow: 0 0 10px #0f172a;">
      <h2 style="color: #1e293b; font-family: Inter; font-size: 24px; margin-bottom: 16px;">Login</h2>
      <form>
        <div style="margin-bottom: 16px;">
          <input type="email" placeholder="Email" style="width: 100%; padding: 12px; border: none; border-radius: 8px; background: #f8fafc; color: #1e293b; font-family: Inter;">
        </div>
        <div style="margin-bottom: 16px;">
          <input type="password" placeholder="Password" style="width: 100%; padding: 12px; border: none; border-radius: 8px; background: #f8fafc; color: #1e293b; font-family: Inter;">
        </div>
        <button type="submit" style="width: 100%; padding: 12px 24px; border: none; border-radius: 8px; background: #6366f1; color: #1e293b; font-family: Inter; cursor: pointer;">Login</button>
      </form>
    </div>
  `,
  styles: [`
    .card {
      width: 300px;
      margin: 40px auto;
    }
  `]
})
export class LoginComponent { }